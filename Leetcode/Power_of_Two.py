"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        power = 2
        while power <= n:
            if power == n:
                return True 
            tmp_power = power
            power = power * power
        
        power = tmp_power

        while power <= n:
            if power == n:
                return True 
            power = power * 2
        return False
