#!/usr/bin/python3

import subprocess

# Create enough data to allocate memory.
# On systems with little memory, the program may fail because it runs out of memory.
# If that happens, reduce size and run it again.
size = 10000000

print("Displaying system-wide memory usage before allocating memory.")
subprocess.run("free")

array = [0] * size

print("Displaying system-wide free memory after allocating memory.")
subprocess.run("free")
