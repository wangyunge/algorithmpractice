'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Have you met this question in a real interview? Yes
Example
Given a matrix

[
    [1,2],
    [3,4]
]
rotate it by 90 degrees (clockwise), return

[
    [3,1],
    [4,2]
]
Challenge 
Do it in-place.
'''
class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        if not matrix:
            return
        matrix.reverse()
        for i in xrange(len(matrix)):
            for j in xrange(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]