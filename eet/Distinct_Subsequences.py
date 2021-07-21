'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
        dp[0][0] = 1 if s[0] == t[0] else 1
        for j in range(1, len(s)):
            dp[0][i] = dp[0][i-1] if t[0] != s[j] else dp[0][i-1] + 1

        for i range(1, len(t)):
            for j in range(1, len(s)):
                if t[i] == s[j]:
                    dp[i][j] = dp[j-1][i] + dp[j][i-1]
                else:
                    dp[i][j] = dp[i][j]
        return d[-1][-1]








class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        DP =  [[1 for j in xrange(len(t)+1)] for i in xrange(len(s)+1)]

        for j in xrange(1,len(t)+1):
            DP[0][j] = 0
            for i in xrange(1,len(s)+1):
                if s[i-1] == t[j-1]:
                    DP[i][j] = DP[i-1][j-1] + DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j]
        return DP[len(s)][len(t)]
