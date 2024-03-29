class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0 :
                    dp[i] = min(dp[i], dp[i-c] + 1)
        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1




