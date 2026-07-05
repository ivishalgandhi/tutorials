package main

import "fmt"

// Swap should exchange the values of a and b.
// BUG: a and b are passed by value, so the swap is lost when the function returns.
func Swap(a, b int) {
	temp := a
	a = b
	b = temp
}

func main() {
	x, y := 10, 20
	Swap(x, y)
	fmt.Printf("x = %d, y = %d\n", x, y)
}
