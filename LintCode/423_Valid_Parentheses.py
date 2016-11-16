'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Have you met this question in a real interview? Yes
Example
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        stack = []
        leftTable = {'(':')','{':'}','[':']'}
        rightSet = [')',']','}']
        res = True
        for character in s:
            if character in leftTable:
                stack.append(character)
            if character in rightSet:
                if not stack:
                    return False
                else: 
                    match = stack.pop()
                    if leftTable[match] != character:
                        return False
        if not stack:
            return True
        else:
            return False
def main():
    sol = Solution()
    test = "[()]"
    sol.isValidParentheses(test)
if __name__ == '__main__':
    main()

