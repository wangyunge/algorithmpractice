"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


"""
Note:
BFS for minial removal
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def _is_valid(s):
            stack = []
            left = 0 
            for item in s:
                if item == '(':
                    left += 1
                    stack.append(item)
                elif item == ')'
                    left -= 1

                if left < 0:
                    return False 
            if left == 0:
                return True 
            else:
                return False 



class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        max_len = 0 
        def _dfs(idx,path, left):
            if idx == len(s):
                if left == 0 :
                    res.add(path)
                    max_len = max(max_len, len(path))
            if s[idx] == '('
                _dfs(idx+1, path+'(', left + 1)
                _dfs(idx+1, path, left)
            elif s[idx] == ')':
                if left > 0:
                    _dfs(idx+1, path + ')' , left-1)
                    _dfs(idx+1, path, left)
            else:
                _dfs(idx+1, path + s[idx] , left)
        res_list = []
        for item in list(res):
            if len(item) == max_len:
                res_list.append(item)
        return res_list



