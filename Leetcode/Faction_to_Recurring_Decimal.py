'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Show Hint 
'''
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
        res =str(numerator/denominator)
        numerator = numerator%denominator
        if numerator != 0:
            res += "."
        while numerator != 0:
            if numerator in modTable:
                brace = modTable[numerator]
                break
            else:
                res += str(numerator*10/denominator)
                modTable[numerator] = len(res)-1
                numerator = numerator*10%denominator
        if brace != 0:
            res = res[:brace] + "(" + res[brace:] + ")"
        if sign:
            res = "-" +res 
        return res
