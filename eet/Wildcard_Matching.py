"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        DP = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        DP[0][0] = True
        for i in range(1, len(p)+1):
            DP[i][0] = True if p[i-1] == '*' and DP[i-1][0] else False  # DP[i-1][0] is important
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    DP[i][j] = DP[i-1][j-1] or DP[i-1][j] or DP[i][j-1]
                elif p[i-1] == '?':         # use elif to switch among cases
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = DP[i-1][j-1] and p[i-1]==s[j-1]
        return DP[-1][-1]
