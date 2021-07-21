"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1


Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build the palindrme end for every start
        reach = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s))[::-1]:
                if _check(i, j):
                    reach[j].append(j)
        dp = [idx for idx in range(len(s))]
        dp.append(0) # rr-1 = -1
        for i in range(1, len(s)):
            for rr in reach[i]:
                dp[i] = min(dp[i] , dp[rr-1] + 1)
        return dp[-2]




