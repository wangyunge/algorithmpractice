class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t, s = s, t
        dp = [[False for _ in range(len(s))] for _ in range(len(t))]
        dp[0][0] = t[0] == s[0]
        for j in range(1, len(s)):
            dp[0][j] =  t[0] == s[j] or dp[0][j-1]
        for i in range(1, len(t)):
            for j in range(1, len(s)):
                if dp[i][j-1]:
                    dp[i][j] = True
                else:
                    if t[i] == s[j]:
                        dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

s = "abc", t = "ahbgdc"
