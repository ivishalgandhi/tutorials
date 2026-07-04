package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
	"sync"
)

type seenIDs struct {
	mu  sync.Mutex
	ids map[string]struct{}
}

func newSeen() *seenIDs {
	return &seenIDs{ids: make(map[string]struct{})}
}

func (s *seenIDs) add(id string) bool {
	s.mu.Lock()
	defer s.mu.Unlock()
	if _, ok := s.ids[id]; ok {
		return false
	}
	s.ids[id] = struct{}{}
	return true
}

func main() {
	seen := newSeen()

	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		eventID := r.Header.Get("X-Event-ID")
		if eventID == "" {
			http.Error(w, "missing event id", http.StatusBadRequest)
			return
		}

		if !seen.add(eventID) {
			w.WriteHeader(http.StatusOK)
			fmt.Fprintf(w, "skipped %s", eventID)
			return
		}

		fmt.Fprintf(w, "processed %s", eventID)
	})

	req := httptest.NewRequest(http.MethodPost, "/", strings.NewReader("body"))
	req.Header.Set("X-Event-ID", "evt-123")
	rec := httptest.NewRecorder()
	handler.ServeHTTP(rec, req)
	fmt.Println(rec.Code, rec.Body.String())

	req2 := httptest.NewRequest(http.MethodPost, "/", strings.NewReader("body"))
	req2.Header.Set("X-Event-ID", "evt-123")
	rec2 := httptest.NewRecorder()
	handler.ServeHTTP(rec2, req2)
	fmt.Println(rec2.Code, rec2.Body.String())
}
