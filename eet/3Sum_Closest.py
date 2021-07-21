"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        best = float('inf')
        res = None
        for idx in range(len(nums)):
            left = idx+1
            right = len(nums)-1

            while left < right:
                cur = nums[idx] + nums[left] + nums[right]
                if cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
                else:
                    return target

                if abs(cur-target) < best:
                    best = abs(cur-target)
                    res = cur
        return res

