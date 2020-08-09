"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def _find_median(nums):
            left = 0
            right = len(nums)-1
            while pos != len(nums) // 2:
                pos = _partition(left, right)
                if pos < len(nums) // 2 :
                    left = pos + 1
                if pos > len(nums) // 2 :
                    right = pos - 1
            return pos

        def _partition(left, right):
            x = nums[left]
            pos = left
            for idx in range(left+1, right+1):
                if nums[idx] <= x:
                    pos += 1
                    nums[pos] , nums[idx] = nums[idx], nums[pos]
            nums[pos], nums[left] = nums[left], nums[pos] 
            return pos
        median_pos = _find_mediam(nums)

        res = [0 for _ in range(len(nums))]
        odd = 0 
        even = 3
        for idx in range(len(nums)):
            if idx == median_pos:
                res[1] = nums[median_pos]
            else:
                if nums[idx] > nums[median_pos]:
                    res[odd] = nums[idx]
                    odd += 1
                else:
                    res[even] = nums[idx]
                    even += 1
        return res



