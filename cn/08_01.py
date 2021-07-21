"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13

"""

class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 2, 4]
        if n <=3 :
            return dp[n-1]

        for i in range(3, n):
            cur = dp[0]  + dp[1] + dp[2]
            cur = cur % 1000000007 
            dp[0], dp[1], dp[2] = dp[1], dp[2], cur
        return cur 

