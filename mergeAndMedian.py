#!/usr/bin/python3

import sys

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    len1 = len(nums1)
    len2 = len(nums2)
    pos = 0
    retlist = []
    for val in nums1:
        while (pos < len2):
            if (val < nums2[pos]):
                print("L:",val)
                retlist.append(val)
                break
            else:
                print("J:",nums2[pos])
                retlist.append(nums2[pos])
                pos = pos+1
        if (pos >= len2):
            retlist.append(val) 
    if (pos < len2):
        while (pos < len2):
            retlist.append(nums2[pos])
            pos = pos+1

    print(retlist)

    len1 = len(retlist)
    if len1 % 2 == 0:
        lmid = int(len1/2)
        print("Len1:", len1, "RetList[lmid]:", retlist[lmid], "LMid:", lmid)
        med = (retlist[lmid-1] + retlist[lmid])/2
    else:
        lmid = int(len1//2)
        print("Len1:", len1, "retlist[lmid]:", retlist[lmid])
        med = (retlist[lmid])
    return med

if __name__ == "__main__":
    inarr1 = [int(num) for num in sys.argv[1].split(",")]
    inarr2 = [int(num) for num in sys.argv[2].split(",")]
    x = findMedianSortedArrays(inarr1, inarr2)
    print(x)

