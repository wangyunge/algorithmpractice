
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        dp[0][0] = 1
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                if i == 1:
                    dp[i][0] = 1
                elif dp[i-1][0] or dp[i-2][0]:
                    dp[i][0] = 1
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] | dp[i-2][j] | (p[i-2] == s[j-1] or p[i-2]=='.' and dp[i-1][j-1])
        return dp[-1][-1] == 1





class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp =[[False for _ in range(len(s))] for _ in range(len(p))]
        dp[0][0] = True
        for i in range(0, len(p)):
            if s[i] == '*':
                dp[i+1][0] = dp[i][0]


        for j in range():

        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] == '.' or  p[i] == s[j]:
                    dp[i][j] = dp[i-1][j-1]
                if p[i] == '*':
                    dp[i][j] = dp[i-1][j]  or (dp[i-1][j-1] and s[j]==s[j-1])
        return dp[-1][-1]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]
