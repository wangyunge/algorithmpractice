"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, just return any of them.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator*numerator <0:
            sign = True
        else:
            sign = False
        numerator = -numerator if numerator <0 else numerator
        denominator = -denominator if denominator <0 else denominator
        modTable = {}
        brace = 0
        res =str(numerator/denominator) # Deal weith the integral part
        numerator = numerator%denominator
        if numerator != 0:
            res += "."
        while numerator != 0:  # the fractionl part
            if numerator in modTable:
                brace = modTable[numerator]
                break
            else:
                res += str(numerator*10/denominator)   # might be 0
                modTable[numerator] = len(res)-1
                numerator = numerator*10%denominator
        if brace != 0:
            res = res[:brace] + "(" + res[brace:] + ")"
        if sign:
            res = "-" +res 
        return res