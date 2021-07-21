"""

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 

        # Ierate every items
        for pi in range(len(nums)):
            # Zero is the number which occupies the position the missing number
            if pi == nums[pi]-1:
                continue
            else:
                idx = nums[pi]-1
                # Set nums[idx] = idx and build a linked list
                while idx >= 0 and idx != nums[idx]-1:
                    idx_next = nums[idx]-1
                    nums[idx] = idx+1
                    idx = idx_next

        # Check which number has not been pointed to 
        for pi in range(len(nums)):
            if pi != nums[pi]-1:
                return pi + 1

        # return 0 if there is not missing number. 
        # Corner case
        return 0
        
"""
Note: Gauss' Formula. missing value = expected_sum - actual_sum 
"""
