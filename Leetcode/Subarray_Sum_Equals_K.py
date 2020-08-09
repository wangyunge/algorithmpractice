"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        b = [i for i in nums]
        table = {0: 1}
        for idx in range(1, len(nums)):
            b[idx] = b[idx-1] + nums[idx]
            cnt = table.get(b[idx], 0)
        res = 0
        for item in b:
            diff = item - k
            res += table.get(diff, 0)
            table.setdefault(item , 0)
            table[item] += 1
        return res 



