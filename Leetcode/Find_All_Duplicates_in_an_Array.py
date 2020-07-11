'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

class Solution:
    """
    1. Difference to Find the Duplicate Number is that we can change the number in place.
    2. iterate all the numbers to see what it points to 
    3. to use the pointer in a position , flip it to negative so we can still use the absolute value as pointer.
    """
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for pi in range(len(nums)):
            if nums[abs(nums[pi])-1] < 0: 
                res.append(abs(nums[pi]))
            else:
                nums[abs(nums[pi])-1] = -nums[abs(nums[pi])-1]
        return res

# class Solution:
#     """
#     1. Difference to Find the Duplicate Number is that we can change the number in place.
#     """
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         res = []
#         for pi in range(len(nums)):
#             if nums[pi] < 0: 
#                 continue
#             idx = nums[pi] - 1
#             while idx >= 0 and idx != nums[idx] -1: 
#                 ne_idx = nums[idx] -1
#                 nums[idx] = -(idx + 1)
#                 if nums[ne_idx] < 0:
#                     res.append(-nums[ne_idx])
#                     break
#                 idx = ne_idx
#         return res

