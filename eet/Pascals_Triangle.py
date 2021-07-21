'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Subscribe to see which companies asked this question
'''
class Solution(object):
    import math
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for rowNum in xrange(0,numRows):
            row =[]
            for index in xrange(0,rowNum+1):
                row.append(self.combination(rowNum,index))
            res.append(row)
        return res
    def combination(self,m,n):
        if m==n or n==0:
            return 1
        Num = math.factorial(m)
        Den = math.factorial(m-n)*math.factorial(n)
        return Num/Den