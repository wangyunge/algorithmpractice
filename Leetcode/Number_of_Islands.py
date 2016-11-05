'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        self.visited = set()
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in self.visited:
                    self.addAllLands((i,j))
                    res +=1
        return res

    def addAllLands(self,landingPot):
        stack = []
        stack.append(landingPot)
        while stack:
            pot = stack.pop()
            if self.grid[pot[0]][pot[1]] == '1' and pot not in self.visited:
                self.visited.add(pot)
                if pot[0]-1 >=0:
                    stack.append((pot[0]-1,pot[1]))
                if pot[0]+1 < len(self.grid):
                    stack.append((pot[0]+1,pot[1]))
                if pot[1]-1 >=0:
                    stack.append((pot[0],pot[1]-1))
                if pot[1]+1 < len(self.grid[0]):
                    stack.append((pot[0],pot[1]+1))
def main():
    test = ["11110","11010","11000","00000"]
    sol = Solution()
    res = sol.numIslands(test)
if __name__ == '__main__':
    main()