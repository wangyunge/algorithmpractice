"""
min,
dp[i-K] + 1
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(1, n+1)]
        for i in range(1, n+1):
            k = 1
            kk = 1
            while kk <= i:
                dp[i] = min(dp[i], dp[i-kk]+1)
                k += 1
                kk = k*k
        return dp[-1]
