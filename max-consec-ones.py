#!/usr/bin/python3
import sys

 
def longestOnes( nums, k):
    zerocount = 0
    left = 0
    maxonecount = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zerocount += 1
        
        while zerocount > k:
            if nums[left] == 0:
                zerocount -= 1
            left += 1

        maxonecount = max(maxonecount, right - left + 1)

if __name__ == "__main__":

    inarr = [int(num) for num in sys.argv[1].split(",")]
    fm = int(sys.argv[2])

