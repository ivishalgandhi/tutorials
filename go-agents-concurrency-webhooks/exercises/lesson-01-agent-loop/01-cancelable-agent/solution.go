package main

import (
	"context"
	"fmt"
	"time"
)

// Sense simulates reading from the environment.
func Sense(ctx context.Context) (string, error) {
	if err := ctx.Err(); err != nil {
		return "", err
	}
	time.Sleep(10 * time.Millisecond)
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
	if err := ctx.Err(); err != nil {
		return err
	}
	time.Sleep(5 * time.Millisecond)
	fmt.Println("action:", action)
	return nil
}

// RunAgent runs the sense-decide-act loop until it is cancelled or reaches maxIterations.
func RunAgent(ctx context.Context, maxIterations int) error {
	for i := 0; i < maxIterations; i++ {
		if err := ctx.Err(); err != nil {
			return fmt.Errorf("agent cancelled: %w", err)
		}

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
	err := RunAgent(ctx, 10000)
	fmt.Printf("elapsed: %s, err: %v\n", time.Since(start), err)
}
