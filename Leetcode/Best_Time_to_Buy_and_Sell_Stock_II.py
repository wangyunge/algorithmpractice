'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        valley = peak = 0

        if len(prices) <= 1:
            return res
        for i in xrange(1,len(prices)):
            if peak >= valley:
                if prices[peak] <= prices[i]:
                    peak = i
                else:
                    res += prices[peak] - prices[valley]
                    valley = i
            if peak <= valley:
                if prices[valley] >= prices[i]:
                    valley = i
                else:
                    peak = i
        if peak == len(prices)-1:
            res += prices[peak] - prices[valley]
        return res
def main():
    sol = Solution()
    test = [2,4,1]
    res = sol.maxProfit(test)
    print res
if __name__ == '__main__':
    main()    
