'''
Given a roman numeral, convert it to an integer.

The answer is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        num = int(s)
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        if s == "":
            return 0
        for charactor in s:
            