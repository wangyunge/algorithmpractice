'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        DP = [ False for i in xrange(len(s)+1)]
        DP[0] = True
        for i in xrange(len(s)+1):
            for j in xrange(i):
                if DP[j] and s[j:i] in wordDict:
                    DP[i] = True
        return DP[-1]
"""
Note: Add a header to make the recurrence equation valid.
"""
