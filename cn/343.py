class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(n+1):
            for k in range(1, i):
                dp[i] = max(dp[i], max(dp[i-k], i-k) * k)
        return dp[-1]