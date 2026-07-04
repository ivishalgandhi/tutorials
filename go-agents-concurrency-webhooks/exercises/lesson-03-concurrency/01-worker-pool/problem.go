package main

import (
	"fmt"
	"sync"
	"time"
)

// Job represents a single unit of work.
type Job struct {
	ID   int
	Name string
}

// Result reports the outcome of a job.
type Result struct {
	ID    int
	Value string
}

// processJob simulates doing work. In a real agent this might call an API.
func processJob(job Job, wg *sync.WaitGroup, results chan<- Result) {
	defer wg.Done()

	// BUG: this goroutine is created once per job, with no limit on concurrency.
	time.Sleep(50 * time.Millisecond)
	results <- Result{ID: job.ID, Value: fmt.Sprintf("processed %s", job.Name)}
}

func main() {
	jobs := []Job{
		{ID: 1, Name: "job-1"},
		{ID: 2, Name: "job-2"},
		{ID: 3, Name: "job-3"},
		{ID: 4, Name: "job-4"},
		{ID: 5, Name: "job-5"},
		{ID: 6, Name: "job-6"},
	}

	results := make(chan Result, len(jobs))
	var wg sync.WaitGroup

	for _, job := range jobs {
		wg.Add(1)
		go processJob(job, &wg, results)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		fmt.Println(result.Value)
	}
}
