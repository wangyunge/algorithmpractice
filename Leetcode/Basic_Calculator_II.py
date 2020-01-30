"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
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
        if not s:
            return 0
        sign = "+"
        res = 0
        val_stack = []
        digit_value = 0
        i = 0
        for cha in s:
            i += 1
            if cha.isdigit():
                digit_value = digit_value * 10 + int(cha)
            if cha == ' ':
                continue
            if not cha.isdigit() or i == len(s):
                if sign == '+':
                    val_stack.append(digit_value)
                if sign == '-':
                    val_stack.append(-digit_value)
                if sign == '*':
                    val_stack.append(val_stack.pop()*digit_value)
                if sign == '/':
                    if digit_value == 0:
                        return
                    val_stack.append(int(float(val_stack.pop())/digit_value))
                digit_value = 0
                sign = cha

        if sign == '+':
            val_stack.append(digit_value)
        if sign == '-':
            val_stack.append(-digit_value)
        if sign == '*':
            val_stack.append(val_stack.pop()*digit_value)
        if sign == '/':
            if digit_value == 0:
                return
            val_stack.append(int(float(val_stack.pop())/digit_value))
        for val in val_stack:
            res += val 
        return res

def main():
    in_put = "14-3/2"
    sol = Solution()
    ret = sol.calculate(in_put)

if __name__ == '__main__':
    main()    



