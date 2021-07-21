"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false


Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = '#' + s
        p = '#' + p
        DP = [[0 for _ in range(len(s))] for _ in range(len(p))]
        DP[0][0] = 1


        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[i] == '.':
                    DP[i][j] = DP[i-1][j-1]
                elif p[i] == s[j]:
                    DP[i][j] = DP[i-1][j-1]
                elif p[i] == '*':
                    DP[i][j] = DP[i][j-1] or DP[i][j-2]
                    (DP[i-1][j] and (s[i] == s[i-1] or s[p[j-1]=='.'))
        return DP[-1][-1]











