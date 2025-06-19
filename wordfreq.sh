#!/usr/bin/bash
n=0
maxfreq=0
while read line; do
    for f in $line; do
	if [[ ${wc[$f]} = "" ]]; then
	    wc[$f]=1
	else
	    wc[$f]=${wc[$f]}+1;
	fi
	# if [ $n < ${wc[$f]} ]; then
	    # n = ${wc[$f]}
	    # maxfreq = $f
	# fi
	echo $f
    done
done < $1
# echo "MaxFreqWord=$maxfreq Frequency:$n"
