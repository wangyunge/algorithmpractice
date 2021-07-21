class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        sold = 0
        hold = -prices[0] - fee
        for i in range(1, len(prices)):
            last_sold = sold
            sold = max(sold, hold + prices[i])
            hold = max(hold, last_sold - prices[i] - fee)
        return sold
