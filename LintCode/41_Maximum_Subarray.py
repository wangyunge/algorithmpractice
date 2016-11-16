'''
Given an array of integers, find a contiguous subarray which has the largest sum.

 Notice

The subarray should contain at least one number.

Have you met this question in a real interview? Yes
Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        res = 0
        local = 0
        negCount = 0
        for i in nums:
            if i < 0:
                negCount += 1
            if local + i > 0:
                local += i
            else:
                local = 0
            res = max(local,res)
        res = nums[0] if len(nums) == negCount else res
        return res