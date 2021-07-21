class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def _dfs(i, j, p):
            if p == len(word) - 1:
                self.res = True
                return True
            if not self.res and i-1 >= 0 and board[i-1][j] == word[p+1]:
                save = board[i-1][j]
                board[i-1][j] = ''
                _dfs(i-1, j, p+1)
                boadr[i-1][j] = save
            if not self.res and i+1 <= len(board)-1 and board[i+1][j] == word[p+1]:
                save = board[i+1][j]
                board[i+1][j] = ''
                _dfs(i+1, j, p+1)
                board[i+1][j] = save
            if not self.res and j>= 0 and board[i][j-1] == word[p+1]:
                save = board[i][j-1]
                board[i][j-1] = ''
                _dfs(i, j-1, p+1)
                board[i]


            else:
                return False




