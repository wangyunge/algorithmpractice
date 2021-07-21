"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

import copy 
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DP = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        DP[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            DP[i][0] = DP[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            DP[0][j] = DP[0][j-1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]
        return DP[-1][-1] 

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0
        DP = deepcopy(grid)
        for i in range(len(grid)-2, -1, -1):
            DP[i][len(grid[0])-1] = 


    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        res = float('inf')
        DP = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def _dfs(i, j, path_sum):
            if i == len(grid[0]) and j == len(grid) :
                res = min(res, path_sum)
            if i < len(grid[0]):
                if DP[i+1][j] != -1:
                    a = DP[i+1][j] +
                _dfs(i+1, j, path_sum + grid[i][j])
            if j < len(grid):
                _dfs(i, j+1, path_sum + grid[i][j])



