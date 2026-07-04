package main

import (
	"fmt"
	"time"
)

// printer writes numbers to out until done is closed.
func printer(out chan<- int, done <-chan struct{}) {
	defer close(out)
	for i := 1; ; i++ {
		select {
		case <-done:
			return
		case out <- i:
			time.Sleep(20 * time.Millisecond)
		}
	}
}

func main() {
	nums := make(chan int)
	done := make(chan struct{})

	go printer(nums, done)

	go func() {
		time.Sleep(100 * time.Millisecond)
		close(done)
	}()

	for n := range nums {
		fmt.Println(n)
	}

	fmt.Println("stopped cleanly")
}
