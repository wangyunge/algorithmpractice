"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        hh = []
        for i in range(len(matrix)):
            heapq.heappush(hh, (matrix[0][i],i,0))
        num = 0
        while num < k:
            res, col, row = heapq.heappop(hh)
            if row+1 < len(matrix):
                heapq.heappush(hh, (matrix[row+1][col],col, row+1))
            num += 1
        return res


