'''
Given a boolean 2D matrix, find the number of islands.

 Notice

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Have you met this question in a real interview? Yes
Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
'''
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        res = 0
        if not grid:
            return res
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    while stack:
                        pot = stack.pop()
                        if grid[pot[0]][pot[1]] == 1:
                            if pot[0]-1 >= 0:
                                stack.append((pot[0]-1,pot[1]))
                            if pot[0]+1 < len(grid):
                                stack.append((pot[0]+1,pot[1]))
                            if pot[1]-1 >=0:
                                stack.append((pot[0],pot[1]-1))
                            if pot[1]+1 < len(grid[0]):
                                stack.append((pot[0],pot[1]+1))
                            grid[pot[0]][pot[1]] = 3
                    res += 1
        return res