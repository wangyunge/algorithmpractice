'''
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

"""
Note:
1. You can Sell and Buy at the same day.
2. Keep recording the max profit while holding the stocks(means you can sell the next day), when you take last transcation.


                t[i][j] = Math.max(t[i][j - 1], prices[j] + tmpMax); # Sell before or Sell now
                tmpMax =  Math.max(tmpMax, t[i - 1][j] - prices[j]); # Buy before or buy now
"""





class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(prices)] for _ in range(k)]
        b_max = float('-inf')
        for j in range(1,len(prices)):
            dp[0][j] = max(dp[0][j-1], b_max + prices[j])
            b_max = max(b_max, 0-prices[j])

        for i in range(1,k):
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], b_max + prices[j])
                b_max = max(b_max, dp[i-1][j]-prices[j])
        return dp[-1][-1]



