class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(max(n+1, 4))]
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], dp[i-j]*dp[j], dp[i-j]*j, (i-j)*j)
        return dp[n]
