#!/bin/bash

usage() {
	exec >&2
	echo "Usage: $0 [-m] <maximum number of processes>
    1. Save performance information to a file named 'cpuperf.data'
        * The number of entries is <maximum number of processes>
        * Each line has the format '<number of processes> <average turnaround time [s]> <throughput [processes/s]>'
    2. Create a graph of average turnaround time from the performance information and save it to 'avg-tat.jpg'
    3. Create a throughput graph and save it to 'throughput.jpg'
    
    The -m option is passed directly to the multiload.sh program."
	exit 1
}

measure() {
	local nproc=$1
	local opt=$2
	bash -c "time ./multiload.sh $opt $nproc" 2>&1 | grep real | sed -n -e 's/^.*0m\([.0-9]*\)s$/\1/p' | awk -v nproc=$nproc '
BEGIN{
    sum_tat=0
}
(NR<=nproc){
    sum_tat+=$1
}
(NR==nproc+1) {
    total_real=$1
}
END{
    printf("%d\t%.3f\t%.3f\n", nproc, sum_tat/nproc, nproc/total_real)    
}'
}

while getopts "m" OPT; do
	case $OPT in
	m)
		MEASURE_OPT="-m"
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

rm -f cpuperf.data
MAX_NPROC=$1
for ((i = 1; i <= MAX_NPROC; i++)); do
	measure $i $MEASURE_OPT >>cpuperf.data
done

./plot-perf.py $MAX_NPROC
