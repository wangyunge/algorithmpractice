'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

 Notice

You can only move either down or right at any point in time.

Have you met this question in a real interview? Yes
'''
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid:
            return 0
        for i in xrange(1,len(grid)):
            grid[i][0] = grid[i-1][0]+grid[i][0]
        for j in xrange(1,len(grid[0])):
            grid[0][j] = grid[0][j-1]+grid[0][j]
        for i in xrange(1,len(grid)):
            for j in xrange(1,len(grid[0])):
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[len(grid)-1][len(grid[0])-1]