'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Subscribe to see which companies asked this question

Show Tags
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.formed = False
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.DFS(0,0,0)
        return self.formed
    def DFS(self,index_1,index_2,index_3):
        if index_3 == len(self.s3):
            if index_1 == len(self.s1) and index_2 == len(self.s2):
                self.formed  = True
        else:
            if index_1 < len(self.s1) and self.s1[index_1] == self.s3[index_3]:
                self.DFS(index_1+1,index_2,index_3+1)
            if index_2 < len(self.s2) and self.s2[index_2] == self.s3[index_3]:
                self.DFS(index_1,index_2+1,index_3+1)
class DPSuolution(object):
    def isInterleave(self,s1,s2,s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l3 != l1 + l2:
            return False
        DP = [[True for _ in xrange(0,l1+1)] for _ in xrange(0,l2+1)]
        for i in xrange(1, l1+1):
            DP[0][i] = DP[0][i-1] and s1[i-1] == s3[i-1]
        for i in xrange(1,l2+1):
            DP[i][0] = DP[i-1][0] and s2[i-1] == s3[i-1]
        for i in xrange(1,l1+1):
            for j in xrange(1,l2+1):
                DP[j][i] = (DP[j-1][i] and s2[j-1] == s3[i+j-1]) or  
