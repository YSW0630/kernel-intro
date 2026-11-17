package main

import "fmt"

func main() {
	// Accessing nil always fails and causes a page fault.
	var p *int = nil
	fmt.Println("Before invalid memory access")
	*p = 0
	fmt.Println("After invalid memory access")
}
