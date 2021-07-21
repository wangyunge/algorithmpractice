class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1, n):
            pick = min(dp[i2]* 2, dp[i3] * 3, dp[i5] * 5)
            if pick == dp[i2] * 2:
                i2 += 1
            if pick == dp[i3] * 3:
                i3 += 1
            if pick == dp[i5] * 5:
                i5 += 1
            dp[i] = pick
        return dp[-1]
