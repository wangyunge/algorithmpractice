class Solution(object):
    def uniquePathsWithObstacles(self, Grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not Grid:
            return 0
        dp = [[1-Grid[i][j] for j in range(len(Grid[0]))] for i in range(len(Grid))]
        for i in range(1, len(Grid)):
            dp[i][0] = 1 if Grid[i][0] == 0 and dp[i-1][0] == 1 else 0
        for j in range(1, len(Grid[0])):
            dp[0][j] = 1 if Grid[0][j] == 0 and dp[0][j-1] == 1 else 0
        for i in range(1, len(Grid)):
            for j in range(1, len(Grid[0])):
                if Grid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


