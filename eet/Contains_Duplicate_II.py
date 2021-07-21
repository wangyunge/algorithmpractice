'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if not nums:
        #     return False
        # for i in xrange(0, len(nums)):
        #     right = min(i + k + 1, len(nums))
        #     for j in xrange(i+1, right):
        #         if nums[i] == nums[j]:
        #             return True 
        # return False

        location_table = {}
        for i in xrange(len(nums)):
            if nums[i] in location_table:
                if asb(location_table[nums[i]] - i) <= k:
                    return True 
                    
            location_table[nums[i]] = i 
        return False