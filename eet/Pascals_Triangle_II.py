'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

Subscribe to see which companies asked this question
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for index in xrange(0,rowIndex+1):
            res.append(self.combination(rowIndex,index))
        return res
    def combination(self,m,n):
        if m==n or n==0:
            return 1
        Num = math.factorial(m)
        Den = math.factorial(m-n)*math.factorial(n)
        return Num/Den