'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O''s into 'X''s in that surrounded region.

Have you met this question in a real interview? Yes
Example
X X X X
X O O X
X X O X
X O X X
After capture all regions surrounded by 'X', the board should be:

X X X X
X X X X
X X X X
X O X X
'''
class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        if not board:
            return board
        height = len(board)
        width = len(board[0])
        for i in xrange(height):
            for j in xrange(width):
                if board[i][j] == 'O':
                    stack = [(i,j)]
                    capture = []
                    escape = False
                    while stack:
                        pot = stack.pop()
                        if board[pot[0]][pot[1]] == 'O':
                            capture.append(pot)
                            if pot[0]-1 >= 0:
                                stack.append((pot[0]-1,pot[1]))
                            else:
                                escape = True
                            if pot[0]+1 < len(board):
                                stack.append((pot[0]+1,pot[1]))
                            else:
                                escape = True
                            if pot[1]-1 >=0:
                                stack.append((pot[0],pot[1]-1))
                            else:
                                escape = True
                            if pot[1]+1 < len(board[0]):
                                stack.append((pot[0],pot[1]+1))
                            else:
                                escape = True
                            if escape:
                                break
                    if not escape:
                        for pot in capture:
                            board[pot[0]][pot[1]] = 'X'
