#!/usr/bin/python3

import sys
import plot_sched


def usage():
    print(
        """Usage: {} <maximum number of processes>
    * Create performance graphs from the "perf.data" file containing cpuperf program results.
    * Save a graph of average turnaround time to "avg-tat.jpg".
    * Save a throughput graph to "throughput.jpg".""".format(progname, file=sys.stderr)
    )
    sys.exit(1)


progname = sys.argv[0]

if len(sys.argv) < 2:
    usage()

max_nproc = int(sys.argv[1])
plot_sched.plot_avg_tat(max_nproc)
plot_sched.plot_throughput(max_nproc)
