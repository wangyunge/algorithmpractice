'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

 Notice

A word is defined as a character sequence consists of non-space characters only.

Have you met this question in a real interview? Yes
Example
Given s = "Hello World", return 5.
'''
class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        s = s.strip()
        for i in xrange(len(s)):
            if s[-(i+1)] == " ":
                return i
        return len(s)