'''
Determine whether a Sudoku is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character ..

 Notice

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Have you met this question in a real interview? Yes
Clarification
What is Sudoku?

http://sudoku.com.au/TheRules.aspx
https://zh.wikipedia.org/wiki/%E6%95%B8%E7%8D%A8
https://en.wikipedia.org/wiki/Sudoku
http://baike.baidu.com/subview/961/10842669.htm
Example
The following partially filed sudoku is valid.

Valid Sudoku
'''
class Solution:        
	def isValidSudoku(self, board):
	    seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
	                for i, row in enumerate(board)
	                for j, c in enumerate(row)
	                if c != '.'), [])
	    return len(seen) == len(set(seen))