package main

import (
	"strings"

	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	result := make(map[string]int)
	flds := strings.Fields(s)
	for _, v := range flds {
		result[v] += 1
	}
	return result
}

func main() {
	wc.Test(WordCount)
}
