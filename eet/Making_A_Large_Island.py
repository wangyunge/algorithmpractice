"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.
"""

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def _union_res(i, j):
            area = 0
            if i >= len(grid) or i < 0 or j >= len(grid[[0]]) or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            elif grid[i][j] == 1:
                grid[i][j] = 0
                area =  _union_res(i+1, j) + _union_res(i-1, j) + _union_res(i, j+1) + _union_res(i, j-1)
                grid[i][j] = 1
            return area

        def _lsland(grid):
            this_max = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        this_max = max(this_max, _union_res(i,j))
            return this_max


        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = 1:
                    res = max(res, _island(grid))
                    grid[i][j] = 0
        return res
"""
Note:
Exchange Space for Time. 
"""