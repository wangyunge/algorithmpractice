'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Have you met this question in a real interview? Yes
Example
Given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''
class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
    	self.n = n
    	self.res = []
    	self.DFS(0,0,"")
    	return self.res
        
    def DFS(self,left,right,res):
    	if right < left:
    		self.DFS(left,right+1,res+")")
    	if left < self.n:
    		self.DFS(left+1,right,res+"(")
    	if right == left and right == self.n:
    		self.res.append(res)