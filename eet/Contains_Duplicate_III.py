'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        window_table = {}
        window_size = t + 1
        for i in xrange(len(nums)):
            table_index = nums[i] / window_size
            if table_index in window_table:
                return True 
            if table_index-1 in window_table and abs(nums[i] - window_table[table_index-1]) <= t:
                return True
            if table_index+1 in window_table and abs(nums[i] - window_table[table_index+1]) <= t:
                return True 
            window_table[table_index] = nums[i]
            if i >= k:
                del window_table[nums[i-k] / window_size]
        return False 