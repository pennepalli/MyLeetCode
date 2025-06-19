def threeSum(nums):
    nums.sort()  # Step 1: Sort the list
    result = []
    
    for i in range(len(nums)):
        # Skip duplicate elements for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointer approach
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
    
    return result

