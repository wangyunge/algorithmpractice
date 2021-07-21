"""
abs,t
abs pos k
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        cover = set()
        for i in range(k):
            center = nums[i]
            for j in range()
