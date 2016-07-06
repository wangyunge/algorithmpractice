'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Subscribe to see which companies asked this question
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        elif int(s[0]) > 26 or int(s[0])<1:
            return 0
        DP = {}
        DP[0] = 1
        DP[-1] = 1
        for i in xrange(1,len(s)):
            if int(s[i]) > 26 or int(s[i])<1:
                return 0
            if int(s[i-1:i+1]) <27:
                DP[i] = DP[i-1] + DP[i-2]
            else:
                DP[i] = DP[i-1]
        return DP[len(s)-1]