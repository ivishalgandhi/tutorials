package main

import (
	"fmt"
	"time"
)

// BUG: there is no way to stop this goroutine.
func printer(out chan<- int) {
	defer close(out)
	for i := 1; ; i++ {
		out <- i
		time.Sleep(20 * time.Millisecond)
	}
}

func main() {
	nums := make(chan int)
	go printer(nums)

	time.Sleep(100 * time.Millisecond)

	// BUG: we cannot drain the channel because printer never closes it.
	fmt.Println("stopping")
}
