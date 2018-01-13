'''
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

Have you met this question in a real interview? Yes
Example
For s1 = "aabcc", s2 = "dbbca"

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1)+len(s2):
            return False
        DP = [[True] * (len(s2)+1) for i in xrange(len(s1)+1)]
        for a in xrange(1,len(s1)+1):
            DP[a][0] = DP[a-1][0] and s1[a-1] == s3[a-1]
        for b in xrange(1,len(s2)+1):
            DP[0][b] = DP[0][b-1] and s2[b-1] == s3[b-1]
        for a in xrange(1,len(s1)+1):
            for b in xrange(1,len(s2)+1):
                One = DP[a-1][b] and s1[a-1] == s3[a-1+b]
                Two = DP[a][b-1] and s2[b-1] == s3[a+b-1]
                DP[a][b] = One or Two
        return DP[-1][-1]

    def isInterleave(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.res = False
        self.table = {}
        if s1 
    def DFS(self,s1,s2,s3):
        if s1 == len(self.s1)-1 and s2 == len(self.s2)-1 and s3 == len(self.s3)-1:
            self.res = True
        if s1 < self.s1
            if ()







        return True