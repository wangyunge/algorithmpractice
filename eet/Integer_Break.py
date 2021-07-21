"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [1 for _ in range(n+1)]
        for i in range(n+1):
            for k in range(1, i-1):
                DP[i] = max(DP[i], max(DP[k],k)*max(DP[i-k], i-k))
        return DP[-1]

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [1 for _ in range(n+1)]
        for i in range(n+1):
            for k in range(1, i//2+1):
                DP[i] = max(DP[i], max(DP[k],k)*max(DP[i-k], i-k))
        return DP[-1]


