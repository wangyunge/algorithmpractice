'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

 Notice

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Have you met this question in a real interview? Yes
Example
Given an example [4,4,6,1,1,4,2,5], return 6.
'''
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        hold1 =  float("-inf")
        hold2 = float("-inf")
        sold1 = 0
        sold2 = 0
        for i in prices:
            sold2 = max(sold2,i+hold2)
            hold2 = max(hold2,sold1-i)
            sold1 = max(sold1,i+hold1)
            hold1 = max(hold1,-i)
        return sold2