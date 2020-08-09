"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [0] * (amount + 1)
        for i in range(1, amount+1):
            res = float('inf')
            for one_coin in coins:
                if i - one_coin >= 0 and DP[i-one_coin] != -1:
                    res = min(res, DP[i-one_coin] + 1)
            DP[i] = res if res < float('inf') else -1
        return DP[-1]

