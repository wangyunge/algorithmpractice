'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = len(nums)+1
        left = right = 0
        sUm = nums[0]
        while 1:
            if sUm >= s:
                res = min(res,right-left+1)
                sUm = sUm - nums[left]
                left += 1
            else:
                right +=1
                if right >= len(nums):
                    break
                else:
                    sUm = sUm + nums[right]
        if res == len(nums)+1:
            return 0
        else:
            return res
            