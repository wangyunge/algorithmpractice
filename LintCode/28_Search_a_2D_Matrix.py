'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Have you met this question in a real interview? Yes
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
'''
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        rLeft = 0
        rRight = len(matrix)-1
        while rLeft < rRight-1:
            mid = (rLeft+rRight)/2
            if matrix[mid][0] > target:
                rRight = mid
            elif matrix[mid][0] < target:
                rLeft = mid
            else:
                return True
        row = rRight if matrix[rRight][0] < target else rLeft
        left = 0
        right = len(matrix[0])-1
        while left < right-1:
            mid = (left+right)/2
            if matrix[row][mid] > target:
                right = mid
            elif matrix[row][mid] < target:
                left = mid
            else:
                return True 
        if matrix[row][left] == target or matrix[row][right] == target:
            return True 
        else:
            return False