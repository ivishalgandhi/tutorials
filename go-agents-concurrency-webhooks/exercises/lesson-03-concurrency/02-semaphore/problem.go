package main

import (
	"fmt"
	"io"
	"net/http"
	"sync"
)

// fetchURL downloads a URL and returns its length. In a real agent this might
// call a webhook provider or an LLM API.
func fetchURL(url string, wg *sync.WaitGroup, results chan<- string) {
	defer wg.Done()

	// BUG: no limit on concurrent network calls.
	resp, err := http.Get(url)
	if err != nil {
		results <- fmt.Sprintf("%s error: %v", url, err)
		return
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(io.LimitReader(resp.Body, 1024))
	if err != nil {
		results <- fmt.Sprintf("%s read error: %v", url, err)
		return
	}

	results <- fmt.Sprintf("%s length: %d", url, len(body))
}

func main() {
	urls := []string{
		"https://go.dev",
		"https://pkg.go.dev",
		"https://gobyexample.com",
	}

	results := make(chan string, len(urls))
	var wg sync.WaitGroup

	for _, url := range urls {
		wg.Add(1)
		go fetchURL(url, &wg, results)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		fmt.Println(result)
	}
}
