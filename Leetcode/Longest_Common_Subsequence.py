"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        s1 = 0
        m = len(text1)
        s2 = 0
        n = len(text2)
        res = 0
        def _backtrack(s1, s2, length)
            for i in range(s1, m): 
                for j in range(s2,n):
                    if text1[i] == text2[j]:
                        length += 1
                        res = max(res, length)
                        _backtrack(i, j, length)



class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        DP = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                DP[i][0] = 1
        for j in range(len(text2)):
            if text2[j] == text1[0]:
                DP[0][j] = 1
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] != text2[j]:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])  # DP[i-1][j-1]
                else:
                    DP[i][j] = DP[i-1][j-1] + 1 
        return DP[i][j]

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        DP = [0 for _ in range(len(text2))]
        for j in range(len(text2)):
            if text2[j] == text1[0]:
                DP[j] = 1
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] != text2[j]:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])  # DP[i-1][j-1]
                else:
                    DP[i][j] = DP[i-1][j-1] + 1 
            last_dp =
        return DP[i][j]