'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Have you met this question in a real interview? Yes
Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        DP = [[False for j in xrange(len(p)+1)] for i in xrange(len(s)+1)]
        DP[0][0] = True 
        for j in xrange(1,len(p)+1):
            if p[j-1] == "*":
                DP[0][j] = DP[0][j-1]
        for i in xrange(1,len(s)+1):
            for j in xrange(1,len(p)+1):
                if p[j-1] == "?":
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1] != "*":
                    DP[i][j] = DP[i-1][j-1] and p[j-1] == s[i-1]
                else:
                    DP[i][j] = DP[i][j-1] or DP[i-1][j]
        return DP[len(s)][len(p)]