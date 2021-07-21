class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def _expand(i, j):
            while i >= 0 and j <= len(s)-1:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            return j-i-1, s[i+1:j]
        res = 0
        res_p = ''
        for mid in range(1, len(s)-1):
            l, p = _expand(mid-1, mid)
            if l > res:
                res_p = p
                res = l
            l, p = _expand(mid, mid)
            if l > res:
                res_p = p
                res = l
        return res_p

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        res_str = []
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if i+1 <=j-1 and dp[i+1][j-1] > 0: # two adjacent
                        dp[i][j] = dp[i+1][j-1] + 2
                    elif i=j-1:   # two adjacent
                        dp[i][j] = 2

                if res < dp[i][j]:
                    res = max(res, dp[i][j])
                    res_str = s[i:j+]
        return res


