'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Have you met this question in a real interview? Yes
Example
Given word1 = "mart" and word2 = "karma", return 3.

'''
class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        DP = [[1 for j in xrange(len(word2)+1)] for i in xrange(len(word1)+1)]
        for i in xrange(len(word1)+1):
            DP[i][0] = i
        for j in xrange(len(word2)+1):
            DP[0][j] = j
        for i in xrange(1,len(word1)+1):
            for j in xrange(1,len(word2)+1):
                lastMin = min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])
                DP[i][j] = lastMin+1 if word1[i-1] != word2[j-1] else DP[i-1][j-1]
        return DP[len(word1)][len(word2)]