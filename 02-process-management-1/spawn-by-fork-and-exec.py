#!/usr/bin/python3

import os

ret = os.fork()
if ret == 0:
    os.execve("/bin/echo", ["echo", "Created by fork() and execve()"], {})
elif ret > 0:
    print("Created the echo command")
