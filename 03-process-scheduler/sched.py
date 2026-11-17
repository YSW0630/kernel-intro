#!/usr/bin/python3

import sys
import time
import os
import plot_sched


def usage():
    print(
        """Usage: {} <number of processes>
        * Start the specified number of workload processes concurrently on logical CPU 0. Each consumes CPU resources for about 100 ms; wait for all processes to exit.
        * Write a graph of the results to "sched-<number of processes>.jpg".
        * The graph x-axis is elapsed time [ms] since starting the workload processes; the y-axis is progress [%].""".format(
            progname, file=sys.stderr
        )
    )
    sys.exit(1)


# Work used for preprocessing to estimate a load suitable for the experiment.
# Reduce this value if the program takes too long to run.
# Increase it if the program finishes too quickly.
NLOOP_FOR_ESTIMATION = 100000000
nloop_per_msec = None
progname = sys.argv[0]


def estimate_loops_per_msec():
    before = time.perf_counter()
    for _ in range(NLOOP_FOR_ESTIMATION):
        pass
    after = time.perf_counter()
    return int(NLOOP_FOR_ESTIMATION / (after - before) / 1000)


def child_fn(n):
    progress = 100 * [None]
    for i in range(100):
        for j in range(nloop_per_msec):
            pass
        progress[i] = time.perf_counter()
    f = open("{}.data".format(n), "w")
    for i in range(100):
        f.write("{}\t{}\n".format((progress[i] - start) * 1000, i))
    f.close()
    exit(0)


if len(sys.argv) < 2:
    usage()

concurrency = int(sys.argv[1])

if concurrency < 1:
    print("<concurrency> must be an integer of at least 1: {}".format(concurrency))
    usage()

# Force execution on logical CPU 0.
os.sched_setaffinity(0, {0})

nloop_per_msec = estimate_loops_per_msec()

start = time.perf_counter()

for i in range(concurrency):
    pid = os.fork()
    if pid < 0:
        exit(1)
    elif pid == 0:
        child_fn(i)

for i in range(concurrency):
    os.wait()

plot_sched.plot_sched(concurrency)
