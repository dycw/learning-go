package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (rot rot13Reader) Read(b []byte) (int, error) {
	n, e := rot.r.Read(b)
	for i := 0; i < n; i++ {
		bi := b[i]
		if (bi >= 'A' && bi <= 'M') || (bi >= 'a' && bi <= 'm') {
			b[i] += 13
		} else if (bi >= 'N' && bi <= 'Z') || (bi >= 'n' && bi <= 'z') {
			b[i] -= 13
		}
	}
	return n, e
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
