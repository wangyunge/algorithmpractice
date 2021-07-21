class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not coins or amount == 0:
            return 0
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                k = 1
                while k*coins[i-1] <= j:
                    dp[i][j] += dp[i-1][j-k*coins[i-1]]
                    k += 1
        return dp[-1][-1]
