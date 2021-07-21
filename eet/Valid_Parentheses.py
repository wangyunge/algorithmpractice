"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False 
                match = stack.pop()
                
                if (char == '}' and match != '{') or (char == ']' and match != '[') or (char == ')' and match != '('):
                    
                    return False 
        return len(stack) == 0

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                left -= 1
            if left < 0:
                return False 
        return left == 0 













