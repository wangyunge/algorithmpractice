'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Have you met this question in a real interview? Yes
Example
Given array [3,2,3,1,2], return 1.
'''
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        res = 0
        valley = prices[0] if prices else 0
        for p in prices:
            valley = min(p,valley)
            res = max(res,p-valley)
        return res
