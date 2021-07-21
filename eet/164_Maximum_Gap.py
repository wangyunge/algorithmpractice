'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = max(nums)
        bottom = min(nums)
        N = len(nums)
        width = floor((top-bottom) / (N-1)) + 1
        bucket = [[None, None] for _ in range(N-1)]
        for item in nums:
            idx = (item-bottom) / width
            if not bucket[idx][0]:
                bucket[idx][0] = item 
            if not bucket[idx][1]:
                bucket[idx][1] = item 
            bucket[idx][0] = min(bucket[idx][0], item)
            bucket[idx][1] = max(bucket[idx][1], item)
        last = bottom 
        res = 0
        for s, e in bucket:
            if s:
                res = max(res, s-last)
                last = s
            if e:
                res = max(res, e-last)
                last = e
        return res








