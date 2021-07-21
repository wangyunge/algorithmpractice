"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def _set_zeros(x, y):
            for i in range(len(matrix)):
                if matrix[i][y] != 0:
                    matrix[i][y] = 231
            for j in range(len(matrix[0])):
                if matrix[x][j] != 0:
                    matrix[x][i] = 231

        if matrix:
            for i in range(len(matrix)) :
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        _set_zeros(i, j)
            for i in range(len(matrix)) :
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 231:
                        matrix[i][j] = 0

