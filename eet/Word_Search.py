'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
Subscribe to see which companies asked this question
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.res = False
        self.word = word
        M = len(board)
        N = len(board[0])
        init = []
        for i in xrange(M):
            for j in xrange(N):
                if board[i][j] == word[0]:
                    self.DFS(i,j,1,[(i,j)])
        return self.res

    def DFS(self,x,y,wordIndx,visited):
        if wordIndx == len(self.word):
            self.res = True
            return None
        if x-1 >= 0 and (x-1,y) not in visited and self.board[x-1][y] == self.word[wordIndx]:
            self.DFS(x-1,y,wordIndx+1,visited+[(x-1,y)])
        if x+1 < len(self.board) and (x+1,y) not in visited and self.board[x+1][y] == self.word[wordIndx]:
            self.DFS(x+1,y,wordIndx+1,visited+[(x+1,y)])
        if y-1 >= 0 and (x,y-1) not in visited and self.board[x][y-1] == self.word[wordIndx]:
            self.DFS(x,y-1,wordIndx+1,visited+[(x,y-1)])
        if y+1 < len(self.board[0]) and (x,y+1) not in visited and self.board[x][y+1] == self.word[wordIndx]:
            self.DFS(x,y+1,wordIndx+1,visited+[(x,y+1)])
        return None
'''
Comments:
    Avoid the circles when you are using the depth first search in a graph.
    And we have a Time Limit Exceeded Error for this version.

Update 20200928:
1. The CORE of DFS is using stacking restore the state. Rebuilding the state after existting from last searching can save time. 
2. Mutable , list
'''