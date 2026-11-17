/*

cache

1. For values from 2^2 (4) KiB through 2^2.25 (4.76) KiB, 2^2.5 (5.7) KiB, and so on up to 64 MiB, perform the following:
  1. Allocate a buffer of the corresponding size.
  2. Access every cache line in the buffer sequentially. After reaching the last cache line, return to the first; perform NACCESS memory accesses in total, as specified in the source code.
  3. Record the time required per access.
2. Based on the results from step 1, output a graph to cache.jpg.

*/

package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"os/exec"
	"syscall"
	"time"
)

const (
	CACHE_LINE_SIZE = 64
	// Adjust this value if the program does not work well. On fast machines, too few
	// accesses can produce incorrect values, especially for small buffers. On slow
	// machines, reduce it if the program takes too long.
	NACCESS = 128 * 1024 * 1024
)

func main() {
	_ = os.Remove("out.txt")
	f, err := os.OpenFile("out.txt", os.O_CREATE|os.O_RDWR, 0660)
	if err != nil {
		log.Fatal("openfile() failed")
	}
	defer f.Close()
	for i := 2.0; i <= 16.0; i += 0.25 {
		bufSize := int(math.Pow(2, i)) * 1024
		data, err := syscall.Mmap(-1, 0, bufSize, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_ANON|syscall.MAP_PRIVATE)
		defer syscall.Munmap(data)
		if err != nil {
			log.Fatal("mmap() failed")
		}

		fmt.Printf("Collecting data for buffer size 2^%.2f (%d) KiB...\n", i, bufSize/1024)
		start := time.Now()
		for i := 0; i < NACCESS/(bufSize/CACHE_LINE_SIZE); i++ {
			for j := 0; j < bufSize; j += CACHE_LINE_SIZE {
				data[j] = 0
			}
		}
		end := time.Since(start)
		f.Write([]byte(fmt.Sprintf("%f\t%f\n", i, float64(NACCESS)/float64(end.Nanoseconds()))))
	}
	command := exec.Command("./plot-cache.py")
	out, err := command.Output()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Command execution failed: %q: %q", err, string(out))
		os.Exit(1)
	}
}
