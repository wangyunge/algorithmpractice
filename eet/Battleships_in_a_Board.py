"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:

X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:

...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        res = 0

        if not board:
            return 0

        def _build_ship(i,j):
            board[i][j] = '.'
            if i-1 >= 0 and board[i-1][j] == 'X':
                _build_ship(i-1, j)
            if i+1 < len(board) and board[i+1][j] == 'X':
                _build_ship(i+1, j)
            if j-1 >= 0 and board[i][j-1] == 'X':
                _build_ship(i, j-1)
            if j+1 < len(board[0]) and board[i][j+1] == 'X':
                _build_ship(i, j+1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    _build_ship(i, j)
                    res += 1
        return res



