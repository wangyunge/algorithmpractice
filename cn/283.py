'''
swap while keep the order
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[pos] = nums[pos], nums[idx]
                pos += 1
        for idx in range(pos, len(nums)):
            nums[idx] = 0

