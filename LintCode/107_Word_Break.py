'''
Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

Have you met this question in a real interview? Yes
Example
Given s = "lintcode", dict = ["lint", "code"].

Return true because "lintcode" can be break as "lint code".

'''
class Solution:
    # @param s: A string s
    # @param words: A dictionary of words dict
    def wordBreak(self, s, words):
        DP = [False for i in xrange(len(s)+1)]
        DP[0] = True
        for i in xrange(1,len(s)+1):
            for j in xrange(i):
                if DP[j] and s[j:i] in words:
                    DP[i] = True
                    break
        return DP[len(s)]
    def wordBreak(self, s, words):
        if not s:
            return False
        DP = [False for i in xrange(len(s))]
        for i in xrange(len(s)):
            for w in words:
                if w == s[i-len(w)+1:i+1] and (DP[i-len(w)] or i-len(w) == -1):
                    DP[i] = True

        return DP[-1]
