'''
Validate if a given string is numeric.

Have you met this question in a real interview? Yes
Example
"0" => true

" 0.1 " => true

"abc" => false

"1 a" => false

"2e10" => true

'''
class Solution:
    # @param {string} s the string that represents a number
    # @return {boolean} whether the string is a valid number
    def isNumber(self, s):
        try:
            out = float(s)
            res = True
        except:
            res = False
        return res
        