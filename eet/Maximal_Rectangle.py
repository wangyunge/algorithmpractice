"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        hist = [0] * (len(matrix[0])+1) # Add the tail whitch is the smallest
        for i in range(len(matrix)):
            stack = [-1]
            for j in range(len(matrix[i])+1):
                if j < len(matrix[i]):
                    hist[j] = hist[j] + 1 if matrix[i][j] == '1' else 0

                while hist[j] < hist[stack[-1]] :
                    mid_idx = stack.pop()
                    res = max(res, hist[mid_idx]*(j-stack[-1]-1))
                stack.append(j)
        return res





