package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
)

func main() {
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		eventID := r.Header.Get("X-Event-ID")
		if eventID == "" {
			http.Error(w, "missing event id", http.StatusBadRequest)
			return
		}

		// BUG: duplicate event IDs are not skipped.
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
