'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Have you met this question in a real interview? Yes
Example
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        opera = {"*","+","-","/"}
        for chara in tokens:
            if chara not in opera:
                stack.append(int(chara))
            else:
                theA = stack.pop()
                theB = stack.pop()
                if chara == "+":
                    val = theA + theB
                if chara == "*":
                    val = theA * theB
                if chara == "-":
                    val = theB - theA
                if chara == "/":
                    val = int(float(theB)/theA)
                stack.append(val)
        return stack[0]
def main():
    test = ["-3","9","*"]
    sol = Solution()
    sol.evalRPN(test)
if __name__ == '__main__':
    main()