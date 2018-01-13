'''
Write a program to check whether a given number is an ugly number`.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

 Notice

Note that 1 is typically treated as an ugly number.

Have you met this question in a real interview? Yes
Example
Given num = 8 return true
Given num = 14 return false
'''
class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        if num < 1:
            return False
        while True:
            if num % 2 == 0:
                num = num/2
            elif num % 3 == 0:
                num = num/3
            elif num % 5 == 0:
                num = num/5
            else:
                break
        if num != 1:
            return False 
        else:
            return True 
