#!/usr/bin/python3

import sys

def balanced_partition(nums):

    right_sum = sum(nums)
    if (right_sum  % 2 == 1):
        return None
    print("Sum=", right_sum )

    left_sum = 0
    for pos,val in enumerate(nums):
        left_sum = left_sum + val
        right_sum =  right_sum - val
        if left_sum == right_sum:
           pos = pos + 1
           return [ nums[:pos],nums[pos:]]

    return None

if __name__ == "__main__":
    inarr1 = [int(num) for num in sys.argv[1].split(",")]
    # inarr2 = [int(num) for num in sys.argv[2].split(",")]
    x = balanced_partition(inarr1)
    print(x)

