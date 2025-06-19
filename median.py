#!/usr/bin/python3

import sys

def findMedian(nums):
    """
    :type nums1: List[int]
    :rtype: float
    """
    len1 = len(nums)
    if len1 % 2 == 0:
        lmid = int(len1/2)
        print("Len1:", len1, "Nums[lmid]:", nums[lmid], "LMid:", lmid)
        med = (nums[lmid-1] + nums[lmid])/2
    else:
        lmid = len1//2
        print("Len1:", len1, "Nums[lmid]:", nums[lmid])
        med = (nums[lmid]/2)
    return med

if __name__ == "__main__":
    inarr1 = [int(num) for num in sys.argv[1].split(",")]
    x = findMedian(inarr1)
    print(x)

