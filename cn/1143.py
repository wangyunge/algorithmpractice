class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, len(test1)):
            dp[i][0] = 1 if dp[i-1][0] or text1[i] == test2[0] else 0
        for j in range(1, len(test2)):
            dp[0][j] = 1 if dp[0][j-1] or test2[j] == test1[0] else 0

        for i in range(1, len(test1)):
            for j in range(1, len(test2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

