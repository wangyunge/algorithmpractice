'''
Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

 Notice

Have you met this question in a real interview? Yes
Example
Given n = 3,

You should return the following matrix:

[
  [ 1, 2, 3 ],
  [ 8, 9, 4 ],
  [ 7, 6, 5 ]
]
'''
class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        matrix = [[0]* n for i in xrange(n)]
        left = 0
        right = n
        top = 0
        bottom = 3
        entry = 1
        while entry <= n*n:
            for j in xrange(left,right):
                matrix[top][j] = entry
                entry += 1
            top += 1
            for i in xrange(top,bottom):
                matrix[i][right-1] = entry
                entry += 1
            right -= 1
            for j in range(left,right)[::-1]:
                matrix[bottom-1][j] = entry
                entry += 1
            bottom -= 1
            for i in range(top,bottom)[::-1]:
                matrix[i][left] = entry
                entry += 1
            left += 1
        return matrix
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A   
