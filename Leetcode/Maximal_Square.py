'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0 
        DP = [[0 for j in xrange(len(matrix[i]))] for i in xrange(len(matrix))]



        for i in xrange(len(matrix)):
            DP[i][0] = int(matrix[i][0])
            res = max(res, DP[i][0])
        for j in xrange(len(matrix[0])):
            DP[0][j] = int(matrix[0][j])
            res = max(res, DP[0][j])

        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[i])):
                if int(matrix[i][j]) == 1:
                    DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
                else:
                    DP[i][j] = 0
                res = max(res, DP[i][j])
        return res * res



'''
Note: The define the sub-problem as the maximal size of square can be achieved at point instead of the original problem. The result of the original problem is the maximual value of the dp matrix. 
'''
   