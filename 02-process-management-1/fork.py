#!/usr/bin/python3

import os, sys

ret = os.fork()
if ret == 0:
    print("Child process: pid={}, parent pid={}".format(os.getpid(), os.getppid()))
    exit()
elif ret > 0:
    print("Parent process: pid={}, child pid={}".format(os.getpid(), ret))
    exit()

sys.exit(1)
