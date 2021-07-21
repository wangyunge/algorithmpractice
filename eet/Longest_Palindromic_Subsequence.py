"""

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.

"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s)+2)] for _ in range(len(s)+2)]

        for i in range(1,len(s)+1):
            for j in range(1, len(s)+1)[::-1]:
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j+1] + 2
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
        res = 0
        for i in range(1, len(s)):
            res = max(res, dp[i][i+1], dp[i][i+2])
        return res
"""
Note: design the subtask directly. dp[i][j] as the sub problem of original problem
"""





