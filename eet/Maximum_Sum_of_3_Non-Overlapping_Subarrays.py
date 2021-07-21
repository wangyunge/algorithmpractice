"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.


Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp1 = [0] * len(nums)
        dp1[k-1] = sum[:k]
        for i in range(k, len(nums)):
            dp1[i] = dp[i-1] - nums[i-k] + nums[i]

        dp2 = [0] * len(nums)
        dp2[len(nums)-k] = sum[len(nums)-k:]
        for i in range(len(nums)-k-1, -1, -1):
            dp1[i] = dp[i+1] - nums[i+k] + nums[i]
        res = 0
        window = sum(num[k+1:k+k+1])
        res = dp1[k-1] + window + dp2[k+k+1]
        for i in range(k, len(nums)-k):
            window =
            res = max(res, dp1[i] + window + dp2[i+k])
        return res



