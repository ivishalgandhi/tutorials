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

// worker reads from the jobs channel until it is closed, then exits.
func worker(id int, jobs <-chan Job, results chan<- Result, wg *sync.WaitGroup) {
	defer wg.Done()

	for job := range jobs {
		time.Sleep(50 * time.Millisecond)
		results <- Result{ID: job.ID, Value: fmt.Sprintf("worker %d processed %s", id, job.Name)}
	}
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

	const numWorkers = 3

	jobCh := make(chan Job, len(jobs))
	results := make(chan Result, len(jobs))
	var wg sync.WaitGroup

	// Start a fixed pool of workers.
	for i := 1; i <= numWorkers; i++ {
		wg.Add(1)
		go worker(i, jobCh, results, &wg)
	}

	// Send all jobs, then close the channel to signal shutdown.
	for _, job := range jobs {
		jobCh <- job
	}
	close(jobCh)

	// Close results after all workers are done.
	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		fmt.Println(result.Value)
	}
}
