#!/bin/bash

<<COMMENT
Prints memory information for the demand-paging.py process once per second.
Each line begins with the time at which the information was collected. The remaining fields mean:
   Field 1: Size of the allocated memory region
   Field 2: Size of allocated physical memory
   Field 3: Number of major faults
   Field 4: Number of minor faults
COMMENT

PID=$(pgrep -f "demand-paging\.py")

if [ -z "${PID}" ]; then
	echo "The demand-paging.py process does not exist; start it before running $0." >&2
	exit 1
fi

while true; do
	DATE=$(date | tr -d '\n')
	# -h suppresses the header.
	INFO=$(ps -h -o vsz,rss,maj_flt,min_flt -p ${PID})
	if [ $? -ne 0 ]; then
		echo "$DATE: the demand-paging.py process has exited." >&2
		exit 1
	fi
	echo "${DATE}: ${INFO}"
	sleep 1
done
