"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:

Input: "123"
Output: "121"
Note:

The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n) % 2 == 0:
            mid = len(2) // 2 -1
            stick = n[:mid+1] + n[:mid+1][::-1]
            if n[mid] != '9':
                plus = n[:mid] + str(int(n[mid])+1)  * 2 + n[:mid][::-1]
            else:


