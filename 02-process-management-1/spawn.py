#!/usr/bin/python3

import os

os.posix_spawn("/bin/echo", ["echo", "echo", "Created by posix_spawn()"], {})
print("Created the echo command")
