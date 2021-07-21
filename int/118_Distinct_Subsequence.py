'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Have you met this question in a real interview? Yes
Example
Given S = "rabbbit", T = "rabbit", return 3.
'''
class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        if not S:
            return 0
        if not T:
            return 1
        self.S = S
        self.T = T
        self.res = 0
        for i in xrange(len(self.S)):
            if self.S[i] == self.T[0]:
                self.DFS(i+1,1)
        return self.res
    def DFS(self,s,t):
        if  t == len(self.T):
            self.res += 1
        else:
            for i in xrange(s,len(self.S)):
                if self.S[i] == self.T[t]:
                    self.DFS(i+1,t+1)
    def numDistinct(self,S,T):
        if not T:
            return 1
        if not S:
            return 0
        DP = [[0] * (len(S)+1) for i in xrange(len(T)+1)]
        for j in xrange(len(S)+1):
            DP[0][j] = 1

        for i in xrange(1,len(T)+1):
            for j in xrange(1,len(S)+1):
                if T[i-1] !=S[j-1]:
                    DP[i][j] = DP[i][j-1]
                else:
                    DP[i][j] = DP[i-1][j-1] + DP[i][j-1]
        return DP[-1][-1]
        
