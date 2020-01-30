"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """ 

        stack = [1]
        res = 0
        sign = 1
        digit_val = 0
        for c in s: 
            if c == ' ':
                continue
            if c.isdigit():
                digit_val = digit_val * 10 + int(c)

            elif c == '(':
                stack.append(sign * stack[-1])
                sign = 1
            else:                
                res += stack[-1] * sign * digit_val
                digit_val = 0
                sign = 1
                if c == '+': 
                    continue
                elif c == '-':
                    sign = -1
                elif c == ')':
                    stack.pop()

        res += stack[-1] * sign * digit_val
        return res             

def main():
    in_put = "-(-23-(21-3+1)-9)"
    sol = Solution()
    ret = sol.calculate(in_put)

if __name__ == '__main__':
    main()    
"""
Note: 
1. the sign of this number
2. how to deal with number bigger than 10
"""