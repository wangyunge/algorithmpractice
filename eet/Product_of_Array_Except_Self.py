"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
import copy
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_res = copy.copy(nums)
        right_res  copy.copy(nums)
        n = len(nums)
        product = 1
        for idx in range(1, n):
            left_res[idx] = nums[idx] * left_res[idx-1]
            right_res[n-1-idx] = nums[n-1-idx] * right_res[n-1-idx+1]
        res = copy.copy(left_res)

        # Missing head and missing tail
        for idx in range(1, n-1):
            res[idx] = left_res[idx-1] * right_res[idx+1]

        res[n-1] = left_res[n-2]
        res[0] = right_res[1]
        return res

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [ 0 for _ in xrange(len(nums))]
        right = [ 0 for _ in xrange(len(nums))]

        pi = 1

        for i in xrange(len(nums)):
            left[i] = pi
            pi = pi * nums[i]

        pi = 1

        for i in range(len(nums))[::-1]:
            right[i] = pi
            pi = pi * nums[i]

        for i in xrange(len(nums)):
            nums[i] = left[i] * right[i]

        return nums
