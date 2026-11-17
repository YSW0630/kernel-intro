package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"strconv"
	"syscall"
)

func main() {
	pid := os.Getpid()
	fmt.Println("*** Process virtual address space before memory-mapping testfile ***")
	command := exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err := command.Run()
	if err != nil {
		log.Fatal("failed to execute cat")
	}

	file, err := os.OpenFile("testfile", os.O_RDWR, 0)
	if err != nil {
		log.Fatal("failed to open testfile")
	}
	defer file.Close()

	// Allocate a 5-byte memory region by calling the mmap() system call.
	data, err := syscall.Mmap(int(file.Fd()), 0, 5, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_SHARED)
	if err != nil {
		log.Fatal("mmap() failed")
	}

	fmt.Println("")
	fmt.Printf("Address where testfile is mapped: %p\n", &data[0])
	fmt.Println("")

	fmt.Println("*** Process virtual address space after memory-mapping testfile ***")
	command = exec.Command("cat", "/proc/"+strconv.Itoa(pid)+"/maps")
	command.Stdout = os.Stdout
	err = command.Run()
	if err != nil {
		log.Fatal("failed to execute cat")
	}

	// Modify the contents of the mapped file.
	replaceBytes := []byte("HELLO")
	for i, _ := range data {
		data[i] = replaceBytes[i]
	}
}
