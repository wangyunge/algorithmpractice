"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for item in nums:
            xor = xor ^ item 
        mask = 1
        while xor&mask == 0:
            mask = mask << 1 
        a = 0
        b = 0
        for item in nums:
            if item&mask:
                a = a ^ item 
            else item&mask == 0:
                b = b ^ item 
        return [a, b]