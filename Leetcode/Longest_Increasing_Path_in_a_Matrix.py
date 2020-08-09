"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        if len(matrix[0]) == 0:
            return 0
        dec_DP = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        inc_DP = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for j in range(1, len(matrix[0])):
            if matrix[0][j] > matrix[0][j-1]:
                dec_DP[0][j] = dec_DP[0][j-1] + 1 
        for j in range(0, len(matrix[0])-1)[::-1]:
            if matrix[0][j] > matrix[0][j+1]:
                inc_DP[0][j] = inc_DP[0][j+1] + 1
        for i in range(1, len(matrix)):
            if matrix[i][0] > matrix[i-1][0]:
                dec_DP[i][0] = dec_DP[i-1][0] + 1 
        for i in range(0, len(matrix[0])-1)[::-1]:
            if matrix[i][0] > matrix[i+1][0]:
                inc_DP[i][0] = inc_DP[i+1][0] + 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] > matrix[i-1][j] :
                    last_up = dec_DP[i-1][j] 
                else:
                    last_up = 0
                if matrix[i][j] > matrix[i][j-1] :
                    last_left = dec_DP[i][j-1] 
                else:
                    last_left = 0
                dec_DP[i][j] = max(last_left, last_up) + 1

        for i in range(0, len(matrix)-1)[::-1]:
            for j in range(0, len(matrix[0])-1)[::-1]:
                if matrix[i][j] > matrix[i+1][j] :
                    last_up = inc_DP[i+1][j] 
                else:
                    last_up = 0
                if matrix[i][j] > matrix[i][j+1] :
                    last_left = inc_DP[i][j+1] 
                else:
                    last_left = 0
                inc_DP[i][j] = max(last_left, last_up) + 1
        res = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                res = max(res, inc_DP[i][j] + dec_DP[i][j] -1 )


        return res


def longestIncreasingPath(self, matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))