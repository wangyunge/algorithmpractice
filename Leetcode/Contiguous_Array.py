"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = [1 if item==1 else -1 for item in nums]
        table = {0:-1}
        res = 0
        level = 0
        for idx in range(len(B)):
            level += B[idx]
            if level in table:
                res = max(res, idx - table[level])
            else:
                table[level] = idx
        return res





