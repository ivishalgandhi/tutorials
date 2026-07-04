package main

import (
	"fmt"
	"io"
	"net/http"
	"sync"
)

// fetchURL downloads a URL while holding a semaphore token.
func fetchURL(url string, sem chan struct{}, wg *sync.WaitGroup, results chan<- string) {
	defer wg.Done()

	sem <- struct{}{}        // acquire
	defer func() { <-sem }() // release

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

	const maxConcurrent = 3

	sem := make(chan struct{}, maxConcurrent)
	results := make(chan string, len(urls))
	var wg sync.WaitGroup

	for _, url := range urls {
		wg.Add(1)
		go fetchURL(url, sem, &wg, results)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		fmt.Println(result)
	}
}
