'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)  -3  3
-5  -10 1
10  30  -5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M = len(dungeon)
        N = len(dungeon[0])
        DP = [[0 for i in xrange(N)] for j in xrange(M)]
        DP[0][0] = dungeon[0][0]
        for i in xrange(1,M):
            DP[i][0] = DP[i-1][0] + dungeon[i][0]
        for j in xrange(1,N):
            DP[0][j] = DP[0][j-1] + dungeon[0][j]
        for i in xrange(1,M):
            for j in xrange(1,N):
                DP[i][j] = dungeon[i][j] + max(DP[i-1][j],DP[i][j-1])
        res = 1 if DP[M-1][N-1] >= 0 else -DP[M-1][N-1]+1
        return res
def main():
    sol = Solution()
    test = [[0,-3,-1],[-2,-3,-4],[-5,-2,0]]
    res = sol.calculateMinimumHP(test)
if __name__ == '__main__':
    main()