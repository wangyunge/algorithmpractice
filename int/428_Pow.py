'''
Implement pow(x, n).

 Notice

You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

Have you met this question in a real interview? Yes
Example
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1
'''
class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        res = 1
        if n >0:
            for i in xrange(n):
                res =  res * x
        else:
            n = abs(n)
            for i in xrange(n):
                res  = res * 1.0/x
        return res
    def myPow(self, x, n):
        if n < 0:
            x =  1.0/x
            n = -n
        if n = 0:
            return 1
        if n = 1:
            return x 
        else:
            if n%2 == 0:
                return self.myPow(x*x,n/2)
            else:
                return self.myPow(x*x,n/2)*x