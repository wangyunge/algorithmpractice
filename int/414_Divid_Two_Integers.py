'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return 2147483647

Have you met this question in a real interview? Yes
Example
Given dividend = 100 and divisor = 9, return 11.

'''
class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
    	positive = (divisor > 0) is (dividend > 0)
    	divisor,dividend = abs(divisor),abs(dividend)
    	res = 0
    	while dividend >= divisor:
    		tmp,power = divisor,1
    		while dividend >= tmp:
    			dividend -= tmp
    			res += power
    			power <<= 1
    			tmp <<= 1
    	if not positive:
    		res = -res
		return min(max(-2147483648, res), 2147483647)