"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.


Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.


Note:

The n will be in the range [1, 1000].
"""


import collections
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        queue = collections.deque()
        queue.append((1, 0, 0))
        while queue:
            paper, board, step = queue.popleft()

            # paste
            if paper + board == n:
                return step + 1
            elif paper + board < n:
                queue.append((paper+board, board, step+1))

            # copy
            if paper < n:
                queue.append((paper, paper, step+1))
        return



"""
Approach # 2
DP[i][j] = DP[i][i-j] + 1
minStep = min(minStep, DP[i][j])
DP[i][i] = minStep + 1


Approach # 3
Any DP[i][j] where j < i comes from DP[j][j]. Set new NDP[i] = DP[i][i]
DP[i] = min(DP[i], DP[j] + 1 + (i-j)/j) when i%j == 0

Approach # 4

"""

import collections
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        for i in range(1, n):
            dp[i] = i
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i / j)
        return dp[-1]



