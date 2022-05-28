package main

import (
	"fmt"
	"internal/fmtsort"
)

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}
