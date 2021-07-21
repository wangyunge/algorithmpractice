'''
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
'''
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [float('-inf') for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            for step in range(1, k+1):
                if i-step >= 0:
                    dp[i] = max(dp[i], dp[i-step] + nums[i])
        return dp[-1]

from collections import deque
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        window = deque()
        dp = nums[0]
        window.append((0, dp))
        for i in range(1, len(nums)):
            while window and i - window[0][0] > k:
                window.popleft()
            dp = window[0][1] + nums[i]
            while window and window[-1][1] <= dp:
                window.pop()
            window.append((i, dp))
        return dp
