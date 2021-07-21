class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        left_num = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                left_num += 1
            elif s[i] == ')':
                if left_num > 0:
                    j = len(stack) - 1
                    part = [')']
                    while stack and stack[-1]!= '(':
                        part.append(stack.pop())
                    part.append(stack.pop()) # Valid
                    left_num -= 1
                    stack.append(''.join(part[::-1]))
            else:
                stack.append(s[i])
        for item in stack:
            if item != '(':
                res.append(item)
        return ''.join(res)



