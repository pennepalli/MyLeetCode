#!/usr/bin/python3

import sys

def topKFrequent(nums, k):

    freq_arr = {}
    val = []
    for f in nums:
        if f in freq_arr:
            freq_arr[f] = freq_arr[f]+1
        else:
            freq_arr[f] = 1
    print(freq_arr)
    sorted_dict = sorted(freq_arr.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dict)
    for i,(num,freq) in enumerate(sorted_dict):
        val.append(num)
        if (i >= k-1):
            break
    print (val)
    return val


if __name__ == "__main__":
    inarr1 = [int(num) for num in sys.argv[1].split(",")]
    freq = int(sys.argv[2])
    topKFrequent(inarr1, freq)
