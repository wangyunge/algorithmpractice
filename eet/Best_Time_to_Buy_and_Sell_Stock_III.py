'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''
 class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        (bottom,top,first) = self.maxOne(prices)
        second = max(self.maxOne(prices[0:bottom])[2],self.maxOne(prices[top+1:])[2])
        return first+second
    def maxOne(self,prices):
        res = (0,0,0)
        bottom =  top = 0
        if not prices:
            return res
        for i in xrange(0,len(prices)):
            if prices[i] < prices[bottom]:
                bottom = top = i
            if prices[i] > prices[top]:
                top = i
                diff = prices[top] - prices[bottom]
                res = (bottom,top,diff) if diff > res[2] else res
        return res

        


def main():
    sol = Solution()
    test = [1,2,4,2,5,7,2,4,9,0]
    res = sol.maxProfit(test)
    print res
if __name__ == '__main__':
    main()
        