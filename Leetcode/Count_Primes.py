'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(2,n):
            if self.checkPrime(i):
                res += 1
        return res
        
    def checkPrime(self,n):
        if n ==2:
            return True
        l = math.sqrt(n)
        for i in xrange(2,math.ceil(l)):
            if n%i == 0:
                return False
        return True
def main():
    sol = Solution()
    res = sol.countPrimes(4)
    
if __name__ == '__main__':
    main()