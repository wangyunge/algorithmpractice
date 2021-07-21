"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sell_free = 0
        buy = -prices[0]
        sell_cold = 0
        for i in range(1, len(prices)):
            tmp_sell_free = max(sell_free, sell_cold)
            tmp_buy = max(buy, sell_free - prices[i])
            tmp_cold = buy + prices[i]

            sell_free = tmp_sell_free
            buy = tmp_buy
            sell_cold = tmp_cold
        return max(sell_free, sell_cold)





"""
Note:
f1: Hold stack
f2: not hold stock and free to buy
f3: not hold stack but froozen

state transfer:
new_f1 = max(f1, f2 - prices[i])
new_f2 = max(f2, f3)
new_f3 = f1 + price[i]
"""
