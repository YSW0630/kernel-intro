#!/bin/bash

echo "Displaying system-wide memory usage before creating the file."
free

echo "Creating a new 1 GB file. This causes the kernel to allocate 1 GB of page cache in memory."
dd if=/dev/zero of=testfile bs=1M count=1K

echo "Displaying system-wide memory usage after allocating the page cache."
free

echo "Displaying system-wide memory usage after deleting the file, and therefore the page cache."
rm testfile
free
