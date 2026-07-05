package main

import "fmt"

type Logger struct {
	Prefix string
}

// Log prints a message with the logger's prefix.
// BUG: if the method is called on a nil *Logger, it panics.
func (l *Logger) Log(msg string) {
	fmt.Printf("%s: %s\n", l.Prefix, msg)
}

func main() {
	var l *Logger // nil pointer
	l.Log("hello")
}
