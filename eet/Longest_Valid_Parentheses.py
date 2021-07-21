"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        stack = []
        left = 0
        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(idx)
            elif s[idx] == ')':
                if stack:
                    match = stack.pop()
                    dp[idx] = dp[match-1] + (idx-match+1)
            else:
                raise ValueError("Undefined Character")
        return max(dp)


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        left = 0
        for idx in range(len(s)):
            if s[idx] == '(':
                left += 1
            else:
                left -= 1

            if left == 0:
                res = max(res, idx - start + 1)
            elif left < 0:
                start = idx + 1
                left = 0
        return res

