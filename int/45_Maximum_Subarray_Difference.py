"""
Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest.

Return the largest difference.
The subarray should contain at least one number
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input:[1, 2, -3, 1]
Output:6
Explanation:
The subarray are [1,2] and [-3].So the answer is 6.
Example 2:

Input:[0,-1]
Output:1
Explanation:
The subarray are [0] and [-1].So the answer is 1.
Challenge
O(n) time and O(n) space.
"""



class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0
        DPA = []
        DPB = []
        tmp_min = float('inf')
        tmp_max = float('-inf')
        min_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            max_sum = max(nums[i], max_sum + nums[i])
            tmp_max = max(tmp_max, max_sum)

            min_sum = min(nums[i], min_sum + nums[i])
            tmp_min = min(tmp_min, min_sum)

            DPA.append((tmp_max, tmp_min))


        tmp_min = float('inf')
        tmp_max = float('-inf')
        min_sum = 0
        max_sum = 0
        for i in range(len(nums))[::-1]:
            max_sum = max(nums[i], max_sum + nums[i])
            tmp_max = max(tmp_max, max_sum)

            min_sum = min(nums[i], min_sum + nums[i])
            tmp_min = min(tmp_min, min_sum)

            DPB.append((tmp_max, tmp_min))
        res = float('-inf')
        L = len(nums)
        for idx in range(0, len(nums) - 1):
            amax,amin = DPA[idx]
            bmax,bmin = DPB[L-idx-2]
            res = max(res, amax-bmin, bmax-amin) 
        return res 
