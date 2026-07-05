package main

import "fmt"

type Logger struct {
	Prefix string
}

// Log prints a message with the logger's prefix.
// FIX: handle a nil receiver so the method does not panic.
func (l *Logger) Log(msg string) {
	if l == nil {
		fmt.Println(msg)
		return
	}
	fmt.Printf("%s: %s\n", l.Prefix, msg)
}

func main() {
	var l *Logger // nil pointer
	l.Log("hello")

	// A real logger should still work normally.
	real := &Logger{Prefix: "app"}
	real.Log("world")
}
