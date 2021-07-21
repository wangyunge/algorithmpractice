'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        DP = [[] for i in xrange(len(s)+1)]
        DP[0] = [' ']
        for i in xrange(len(s)+1):
            for j in xrange(i):
                if DP[j] and s[j:i] in wordDict:
                    for word in DP[j]:
                        DP[i].append(word.strip() + ' ' + s[j:i])
        for i in xrange(len(DP[-1])):
            DP[-1][i] = DP[-1][i].strip()
        return DP[-1]