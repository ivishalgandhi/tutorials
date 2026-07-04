package main

import (
	"fmt"
	"net/http"
	"time"
)

// BUG: no graceful shutdown. The server exits immediately on SIGINT.
func main() {
	jobs := make(chan string, 10)

	go func() {
		for j := range jobs {
			time.Sleep(200 * time.Millisecond)
			fmt.Println("processed", j)
		}
	}()

	http.HandleFunc("/webhook", func(w http.ResponseWriter, r *http.Request) {
		jobs <- r.URL.Path
		w.WriteHeader(http.StatusAccepted)
	})

	fmt.Println("listening on :8080")
	// BUG: ListenAndServe cannot be shut down gracefully.
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("server error:", err)
	}
}
