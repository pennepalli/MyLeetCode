import sys

# Rotate Array: Given an array, rotate the array to the right by k steps, where k is non-negative.
# a,b,c,d,e,f,g,h,i,j,k rotate by 4 =>  h,i,j,k,a,b,c,d,e,f,g

def rotate_array(nums, k):
    """
    Rotates an array to the right by k steps.

    Args:
        nums: The array to rotate.
        k: The number of steps to rotate the array to the right.
    """
    n = len(nums)
    k = k % n  # Handle cases where k is larger than the array length

    # Method 1: Using slicing and concatenation (more Pythonic)
    nums[:] = nums[n-k:] + nums[:n-k] # Modifies the list in-place

    # Method 2: Reversing the list
    # reverse(nums, 0, n - 1)
    # reverse(nums, 0, k - 1)
    # reverse(nums, k, n - 1)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Example Usage
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate_array(nums1, k1)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
k2 = 2
rotate_array(nums2, k2)
print(nums2)  # Output: [3, 99, -1, -100]

nums3 = [1,2]
k3 = 3
rotate_array(nums3, k3)
print(nums3) # Output: [2,1]

nums4 = [1,2,3]
k4 = 1
rotate_array(nums4,k4)
print(nums4) #output [3,1,2]
