package main

import (
	"context"
	"fmt"
	"time"
)

// Sense simulates reading from the environment.
func Sense(ctx context.Context) (string, error) {
	// BUG: this function does not respect context cancellation.
	time.Sleep(1 * time.Millisecond)
	return "build", nil
}

// Decide maps an event to an action.
func Decide(event string) string {
	if event == "build" {
		return "compile"
	}
	return "noop"
}

// Act simulates running the action.
func Act(ctx context.Context, action string) error {
	// BUG: this function does not respect context cancellation.
	_ = ctx
	time.Sleep(1 * time.Millisecond)
	fmt.Println("action:", action)
	return nil
}

// RunAgent runs the sense-decide-act loop up to maxIterations times.
func RunAgent(ctx context.Context, maxIterations int) error {
	for i := 0; i < maxIterations; i++ {
		// BUG: check ctx.Err() here so the loop exits when cancelled.

		event, err := Sense(ctx)
		if err != nil {
			return fmt.Errorf("sense: %w", err)
		}

		action := Decide(event)
		if action == "noop" {
			continue
		}

		if err := Act(ctx, action); err != nil {
			return fmt.Errorf("act: %w", err)
		}
	}
	return nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 50*time.Millisecond)
	defer cancel()

	start := time.Now()
	err := RunAgent(ctx, 100)
	fmt.Printf("elapsed: %s, err: %v\n", time.Since(start), err)
}
