package main

import (
	"fmt"
	"net/http"
	"sync"
	"time"
)

type event struct {
	id string
}

func main() {
	events := make(chan event, 10)

	var wg sync.WaitGroup
	for i := 0; i < 3; i++ {
		wg.Add(1)
		go worker(i, events, &wg)
	}

	http.HandleFunc("/webhook", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
			return
		}

		e := event{id: r.Header.Get("X-Event-ID")}

		select {
		case events <- e:
			w.WriteHeader(http.StatusAccepted)
			fmt.Fprintln(w, "accepted")
		default:
			w.Header().Set("Retry-After", "5")
			http.Error(w, "queue full", http.StatusServiceUnavailable)
		}
	})

	fmt.Println("listening on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil && err != http.ErrServerClosed {
		fmt.Println("server error:", err)
	}

	close(events)
	wg.Wait()
}

func worker(id int, events <-chan event, wg *sync.WaitGroup) {
	defer wg.Done()
	for e := range events {
		time.Sleep(200 * time.Millisecond) // simulate work
		fmt.Printf("worker %d processed event %s\n", id, e.id)
	}
}
