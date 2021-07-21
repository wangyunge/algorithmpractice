'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

 Notice

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Have you met this question in a real interview? Yes
Example
Given [1, 9, 2, 5], the sorted form of it is [1, 2, 5, 9], the maximum gap is between 5 and 9 = 4.
'''
class Solution:
     # @param nums: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums2 = sorted(nums)
        res = 0
        for i in xrange(len(nums)):
            res = max(res,abs(nums[i] - nums2[i]))
        return res