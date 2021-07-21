"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:
G
Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = 0
        res = 0
        for item in nums:
            dp = max(item, dp + item)
            res = max(res, dp)
        return res


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        def _dvi(i, j):
            if i == j:
                return nums[i]
            else:
                mid = (i+j)//2
                return _conq(_dvi(i, mid), _dvi(mid+1, j))
        def _conq(a, b):


