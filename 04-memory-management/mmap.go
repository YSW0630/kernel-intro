package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"strconv"
	"syscall"
)

const (
	ALLOC_SIZE = 1024 * 1024 * 1024
)

func main() {
	pid := os.Getpid()
	fmt.Println("*** Memory map before allocating a new memory region ***")
	command := exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err := command.Run()
	if err != nil {
		log.Fatal("failed to execute cat")
	}

	// Allocate a 1 GB memory region by calling the mmap() system call.
	data, err := syscall.Mmap(-1, 0, ALLOC_SIZE, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_ANON|syscall.MAP_PRIVATE)
	if err != nil {
		log.Fatal("mmap() failed")
	}

	fmt.Println("")
	fmt.Printf("*** New memory region: address = %p, size = 0x%x ***\n",
		&data[0], ALLOC_SIZE)
	fmt.Println("")

	fmt.Println("*** Memory map after allocating a new memory region ***")
	command = exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err = command.Run()
	if err != nil {
		log.Fatal("failed to execute cat")
	}
}
