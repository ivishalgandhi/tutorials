package main

import (
	"fmt"
	"net/http"
	"time"
)

// BUG: slow work is done synchronously inside the HTTP handler.
func webhookHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}

	eventID := r.Header.Get("X-Event-ID")

	// Slow work blocks the HTTP response.
	time.Sleep(200 * time.Millisecond)
	fmt.Printf("processed event %s\n", eventID)

	w.WriteHeader(http.StatusOK)
	fmt.Fprintln(w, "ok")
}

func main() {
	http.HandleFunc("/webhook", webhookHandler)
	fmt.Println("listening on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("server error:", err)
	}
}
