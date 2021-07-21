'''
Given a string s, you are allowed to convert it to a palindrome by adding 
characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
'''
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in xrange(len(s)):
            tail = len(s) - 1 - i 
            new_str = s[tail:][::-1] + s
            if checkPalindrome(new_str):
                return new_str
                
    def checkPalindrome(self, s):
        l = 0
        r = len(s)
        res = True
        while l < s:
            if s[l] != s[r]:
                res = False
                break
        return res