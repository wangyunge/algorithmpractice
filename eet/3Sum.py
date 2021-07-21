"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # CC1: Duplicate number in list
        # Duplicate in start index,
        # Duplicate in left and right index
        # CC2:
        if not nums:
            return
        nums.sort()
        res = []
        for start in range(len(nums)-2):
            if start > 0 and nums[start-1] == nums[start]:
                continue
            target = -nums[start]
            left = start + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[start], nums[left], nums[right]])
                    while left < right and  nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    right -= 1
        return res



