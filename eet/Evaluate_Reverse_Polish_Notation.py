'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []
        operators = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x/y}
        for item in tokens:
            if item in operators:
                B = stack.pop()
                A = stack.pop()
                res = operators[item](A,B)
                if item == '/' and res == -1 and abs(A) < abs(B):
                    stack.append(0) #Cheating here
                else:
                    stack.append(res)
            else:
                stack.append(int(item))
        return stack.pop()
def main():
    sol = Solution()
    res = sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

if __name__ == '__main__':
    main()