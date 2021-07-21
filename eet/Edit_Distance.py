# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character
# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i range(1, len(word2)+1):
            dp[i][0] = i
        for j range(1, len(word1) + 1):
            dp[0][j] = j
        for i in range(len(word1+1)):
            for j in range(len(word2+1)):
                if word1[i-1][j-1] == word2[i-1][j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
















class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        DP = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            DP[i][0] = i
        for j in range(len(word2)+1):
            DP[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = min(DP[i-1][j-1], DP[i-1][j]+1)
                else:
                    DP[i][j] = min(DP[i-1][j]+1, DP[i-1][j-1]+1, DP[i][j-1]+1)
        return DP[-1][-1]











class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        DP = [[1 for _ in range(len(word1))] for _ in range(len(word2))]
        DP[0][0] = 0 if word1[0] == word2[0] else 1
        for i in range(1, len(word2)):
            DP[i][0] = DP[i-1][0] + 1
        for i in range(len(word2)):
            if i == 0:
                for j in range(1, len(word1)):

            for j in range(1, len(word1)):
                if word2[j] == word1[i]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min([DP[i-1][j], DP[i][j-1], DP[i-1][j-1]]) + 1
        a = b
        return DP[-1][-1]
