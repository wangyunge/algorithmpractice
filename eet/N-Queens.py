"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        def _dfs(idx, queens):
            if idx == n:
                res.append(queens)
            forbit_set = set()
            for i in range(len(queens)):
                forbit_set.add(queens[i])
                forbit_set.add(queens[i]+(idx-i))
                forbit_set.add(queens[i]-(idx-i))
            for j in range(n):
                if j not in forbit_set:
                    _dfs(idx+1, queens+[j])
        _dfs(0, []) 
        return res