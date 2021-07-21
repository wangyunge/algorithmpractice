'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Have you met this question in a real interview? Yes
Example
Given n = 12, return 3 because 12 = 4 + 4 + 4
Given n = 13, return 2 because 13 = 4 + 9
'''
class Solution:
    # @param {int} n a positive integer
    # @return {int} an integer
    def numSquares(self, n):
        import math
        DP = [n for _ in xrange(n+1)]
        DP[0] = 0
        for i in xrange(1,n+1):
            for j in xrange(1,int(math.sqrt(i))+1):
                DP[i] = min(DP[i],DP[i-j*j]+1)
        return DP[-1]