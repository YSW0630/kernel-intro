#!/usr/bin/python3

import os
import sys
import mmap
from sys import byteorder

PAGE_SIZE = 4096

data = 1000
print("Data value before creating the child process: {}".format(data))
shared_memory = mmap.mmap(-1, PAGE_SIZE, flags=mmap.MAP_SHARED)

shared_memory[0:8] = data.to_bytes(8, byteorder)

try:
    pid = os.fork()
except OSError:
    print("fork() failed", file=sys.stderr)
    sys.exit(1)

if pid == 0:
    data = int.from_bytes(shared_memory[0:8], byteorder)
    data *= 2
    shared_memory[0:8] = data.to_bytes(8, byteorder)
    sys.exit(0)

os.wait()
data = int.from_bytes(shared_memory[0:8], byteorder)
print("Data value after the child process exits: {}".format(data))
