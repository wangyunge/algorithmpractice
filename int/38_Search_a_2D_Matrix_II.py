'''
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.
Have you met this question in a real interview? Yes
Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.
'''
class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0
        row = 0
        column = len(matrix[0])-1
        res = 0
        while row <= len(matrix)-1 and column >= 0:
            if matrix[row][column] == target:
                res += 1
                row += 1
                column -=1
            elif matrix[row][column] < target:
                row += 1
            else:
                column -=1
        return res
