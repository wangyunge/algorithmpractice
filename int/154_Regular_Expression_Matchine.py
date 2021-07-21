'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)
Have you met this question in a real interview? Yes
Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        DP = [[False for j in xrange(len(p)+1)] for i in xrange(len(s)+1)]
        for i in xrange(len(s)+1):
            for j in xrange(len(p)+1):
                if j == 0:
                    if i == 0:
                        DP[i][j] = True 
                elif i == 0:
                    if p[j-1] == "*" and j > 1:
                        DP[i][j] = DP[i][j-2]
                elif p[j-1] == ".":
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1] != "*":
                    DP[i][j] = p[j-1] == s[i-1] and DP[i-1][j-1]
                else:
                    if DP[i][j-2] or DP[i][j-1]:
                        DP[i][j] = True
                    if DP[i-1][j] and j > 1:
                        DP[i][j] = p[j-2] == s[i-1] or p[j-2] == "."
        return DP[len(s)][len(p)]
