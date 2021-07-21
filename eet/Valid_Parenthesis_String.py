'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        start = 0
        for idx in range(len(s)):
            if s[idx] == '(':
                left += 1
            elif s[idx] == ')':
                left -= 1
            elif s[idx] == '*':
                star += 1

            if left < 0 :
                star = left + star
                if star < 0:
                    return False
        if left
'''
Note: Keep track of the range which is always above zero
'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append('(')


# DFS ?

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dp = [[3 for _ in range(len(s))] for _ in range(len(s)//2)]
        def _dfs(idx, left):

            for idx in range(len(s)):
                if s[idx] == '(':
                    left += 1
                elif s[idx] == ')':
                    left -= 1
                elif s[idx] == '*':
                    break
                if left < 0:
                    return False
            if idx != len(s) - 1:
                return  _dfs(idx+1, left) or _dfs(idx+1, left-1) or _dfs(idx+1, left+1)
            elif s[idx] == '*':
                return left == 1 or left == 0
            else:
                return left == 0

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = len(s)


