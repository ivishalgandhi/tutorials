package main

import "fmt"

// Swap exchanges the values stored at the addresses of a and b.
// FIX: pass pointers so the caller's variables are modified.
func Swap(a, b *int) {
	temp := *a
	*a = *b
	*b = temp
}

func main() {
	x, y := 10, 20
	Swap(&x, &y)
	fmt.Printf("x = %d, y = %d\n", x, y)
}
