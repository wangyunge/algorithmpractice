"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.

"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s)) ]
        for i range(len(s))[::-1]:
            dp[i][i] = True
            res += 1
            if s[i] = s[i+1]:

            for j in range(i+1, len(s)):


"""
Notes:  DP dones not save anything as we can save the results when we expand the string.
"""
