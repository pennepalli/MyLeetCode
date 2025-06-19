import sys

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr = {}
    n=0
    for f in nums:
        if f in arr:
            arr[f] = arr[f]+1
        else:
            arr[f]=1
        if arr[f] > n:
            n = arr[f]
            maxv = f
    return n, maxv

if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    num, val = majorityElement(inarr)
    print ("Max Val = ", val, " Frequency: ", num)

