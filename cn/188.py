class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0
        k = min(k, len(prices)//2+1)
        dp = [[[0, 0] for j in range(len(prices))] for i in range(k)]
        dp[0][0][0] = -prices[0]
        dp[0][0][1] = 0
        for j in range(1, len(prices)):
            dp[0][j][0] = max(dp[0][j-1][0], -prices[j])
            dp[0][j][1] = max(dp[0][j-1][1], dp[0][j-1][0]+prices[j])
        for i in  range(1, k):
            dp[i][0][0] = -prices[0]
            dp[i][0][1] = 0
            for j in range(1, len(prices)):
                dp[i][j][0] = max(dp[i][j-1][0], dp[i-1][j-1][1]-prices[j])
                dp[i][j][1] = max(dp[i][j-1][1], dp[i][j-1][0]+prices[j])
        return dp[-1][-1][1]



class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);

        return max(sell[n - 1])

