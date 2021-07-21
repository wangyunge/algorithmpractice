'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Have you met this question in a real interview? Yes
Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
'''
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        dp = {0:1,1:1,2:2}
        if n > 2:
            i = 3
            while i <= n:
                dp[i] = dp[i-1] + dp[i-2]
                i += 1
        return dp[n] 