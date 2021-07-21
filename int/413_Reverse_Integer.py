'''
Reverse digits of an integer. Returns 0 when the reversed integer overflows (signed 32-bit integer).

Have you met this question in a real interview? Yes
Example
Given x = 123, return 321

Given x = -123, return -321

'''
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        sign = 1 if n > 0 else -1
        n = abs(n)
        numList = []
        while n/10 >=1:
            numList.append(n%10)
            n = n/10
        numList.append(n)
        n=0
        for i in numList:
            n = n*10 + i
        n = n * sign
        if n > 2147483647 or n < -2147483648:
            return 0
        else:
            return n
            