#!/usr/bin/python3

import os
import subprocess
import sys
import mmap

ALLOC_SIZE = 100 * 1024 * 1024
PAGE_SIZE = 4096


def access(data):
    for i in range(0, ALLOC_SIZE, PAGE_SIZE):
        data[i] = 0


def show_meminfo(msg, process):
    print(msg)
    print("Output of the free command:")
    subprocess.run("free")
    print("Memory-related information for {}".format(process))
    subprocess.run(["ps", "-orss,maj_flt,min_flt", str(os.getpid())])
    print()


data = mmap.mmap(-1, ALLOC_SIZE, flags=mmap.MAP_PRIVATE)
access(data)
show_meminfo("*** Before creating the child process ***", "parent process")

try:
    pid = os.fork()
except OSError:
    print("fork() failed", file=sys.stderr)
    sys.exit(1)

if pid == 0:
    show_meminfo(
        "*** Immediately after creating the child process ***", "child process"
    )
    access(data)
    show_meminfo("*** After memory access by the child process ***", "child process")
    sys.exit(0)

os.wait()
