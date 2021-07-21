
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            dp[i][0] = True if p[i-1] == '*' and dp[i-1][0] else False

        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '?' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]
        return dp[-1][-1]
