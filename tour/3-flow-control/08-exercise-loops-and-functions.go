package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	var z_old float64
	z := 1.0
	for i := 0; ; i++ {
		z_old = z
		z -= (z*z - x) / (2 * z)
		abs_diff := math.Abs(z - z_old)
		fmt.Println("Guess=", i, "z_old=", z_old, "z=", z, "|diff|=", abs_diff)
		if abs_diff <= 1e-10 {
			return z
		}
	}
}

func main() {
	fmt.Println(Sqrt(2))
}
