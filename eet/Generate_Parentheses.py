"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def _dfs(path, left, rest):
            if left == 0 and rest ==0:
                res.append(path)
            else:
                if rest > 0:
                    _dfs(path + '(', left+1, rest-1)
                if left > 0:
                    _dfs(path + ')', left -1, rest)
        _dfs('', 0, n)
        return res 