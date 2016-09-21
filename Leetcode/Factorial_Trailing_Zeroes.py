'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        power = 0
        res = 0
        while n > pow(5,power):
            power += 1
        power -= 1
        for i in xrange(1,power+1):
            res += (n/pow(5,i))*power
        return res
def main():
    sol = Solution()
    test = 30
    res = sol.trailingZeroes(test)
if __name__ == '__main__':
    main()