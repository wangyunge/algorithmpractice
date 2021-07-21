"""
Compressed DP , NEED the temp varible to store status
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        dp_max = nums[0]
        dp_min = nums[0]
        res = nums[0]
        for item in nums[1:]:
            tdp_max = max(dp_max * item , item, dp_min * item)
            tdp_min = min(dp_max * item , item , dp_min * item)
            dp_max = tdp_max
            dp_min = tdp_min
            res = max(dp_max, res)
        return res

