"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

# Approach 1 : DP
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [idx for idx in range(len(nums))]
        for idx in range(len(nums)):
            for steps in range(1, nums[idx]):
                dp[idx+steps] = min(dp[idx+steps], dp[idx] + 1)
        return dp[-1]

# Approach 2: reach and steps, yes, greedy
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        reach = 0
        boarder = 0
        for idx in range(len(nums)):
            if idx <= reach:
                boarder = max(boarder, nums[idx] + idx)
            else:
                reach = boarder
                step += 1
                boarder = max(boarder, nums[idx] + idx)
        return step

