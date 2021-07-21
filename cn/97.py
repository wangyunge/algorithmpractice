class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        mem = {}
        def _dfs(i, j):
            if i + j == len(s3):
                self.res = True
            if not self.res and (i, j) not in mem:
                if s1[i] == s3[i+j]:
                    _dfs(i+1, j)
            if not self.res and (i, j) not in mem:
                if s2[j] == s3[i+j]:
                    _dfs(i, j+1)
            mem[(i, j)] = self.res
        return self.res


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp =[[False for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        dp[0][0] = True
        for j in range(1, len(s1)+1):
            dp[0][j] = True if s1[j-1] == s3[j-1] and dp[0][j-1] else False
        for i in range(1, len(s2)+1):
            dp[i][0] = True if s2[i-1] == s3[i-1] and dp[i-1][0] else False
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if s1[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
                if s2[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
        return dp[-1][-1]
