"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # CC1: 0 []
        def _dfs(rest, wallet_id):
            if rest == 0:
                return 1
            res = 0
            for idx in range(wallet_id, len(coins)):
                if rest >= coins[idx]:
                    res += _dfs(rest-coins[idx], idx)
            return res
        return _dfs(amount, 0)

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for idx in range(1, amount+1):
            res = 0
            for single in coins:
                if single >= idx:
                    res += dp[idx-single]
            dp[idx] = res
        return dp[-1]

"""
The two codes on superificial comparison look equal, but the Code 1 gives a higher number of solutions that the correct answer.
The reason for this is when we create an amount array from 0...Amount, if we iterate over all the coins a solution
can be added twice. For example to create 7:

When amount is 2 and the coin value is 5, it would be counted as 1 way.
When amount is 5 and the coin value is 2, the number of ways become 2.
The set is either case remains 1 coin of 2 and 1 coin of 5. But the first method adds it twice.
So we create use an outer loop of coins so that a combination once used cannot be used again.

I hope this helps someone stuck at the same issue.
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1 # The base block to sum
        for den in coins:
            for i in range(amount+1):
                if i - den >= 0: # Start from base brick
                    dp[i] += dp[i-den]
        return dp[-1]


