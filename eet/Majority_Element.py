'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        counts = 0
        for element in nums:
            if counts == 0:
                majority = element
                counts += 1
            elif element == majority:
                counts += 1
            else:
                counts -= 1
        return majority