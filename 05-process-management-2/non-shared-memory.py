#!/usr/bin/python3

import os
import sys

data = 1000

print("Data value before creating the child process: {}".format(data))
try:
    pid = os.fork()
except OSError:
    print("fork() failed", file=sys.stderr)
    sys.exit(1)

if pid == 0:
    data *= 2
    sys.exit(0)

os.wait()
print("Data value after the child process exits: {}".format(data))
