#!/usr/bin/python3

import mmap
import time
import datetime

ALLOC_SIZE = 100 * 1024 * 1024
ACCESS_UNIT = 10 * 1024 * 1024
PAGE_SIZE = 4096


def show_message(msg):
    print("{}: {}".format(datetime.datetime.now().strftime("%H:%M:%S"), msg))


show_message(
    "Before allocating a new memory region. Press Enter to allocate a new 100 MiB memory region: "
)
input()

# Allocate a 100 MiB memory region by calling the mmap() system call.
memregion = mmap.mmap(-1, ALLOC_SIZE, flags=mmap.MAP_PRIVATE)
show_message(
    "A new memory region was allocated. Press Enter to access 10 MiB per second, for a total of 100 MiB, in the new memory region: "
)
input()

for i in range(0, ALLOC_SIZE, PAGE_SIZE):
    memregion[i] = 0
    if i % ACCESS_UNIT == 0 and i != 0:
        show_message("Accessed {} MiB".format(i // (1024 * 1024)))
        time.sleep(1)

show_message("Accessed all of the newly allocated memory region. Press Enter to exit: ")
input()
