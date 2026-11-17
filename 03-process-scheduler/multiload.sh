#!/bin/bash

MULTICPU=0
PROGNAME=$0
SCRIPT_DIR=$(cd $(dirname $0) && pwd)

usage() {
	exec >&2
	echo "Usage: $PROGNAME [-m] <number of processes>
    Runs the specified number of workload processes for a fixed duration, then waits for all of them to exit.
    Prints the time taken by each process.
    By default, all processes run on a single logical CPU.

Options:
    -m: Allow each process to run on multiple CPUs."
	exit 1
}

while getopts "m" OPT; do
	case $OPT in
	m)
		MULTICPU=1
		;;
	\?)
		usage
		;;
	esac
done

shift $((OPTIND - 1))

if [ $# -lt 1 ]; then
	usage
fi

CONCURRENCY=$1

if [ $MULTICPU -eq 0 ]; then
	# Restrict workload execution to CPU 0.
	taskset -p -c 0 $$ >/dev/null
fi

for ((i = 0; i < CONCURRENCY; i++)); do
	time "${SCRIPT_DIR}/load.py" &
done

for ((i = 0; i < CONCURRENCY; i++)); do
	wait
done
