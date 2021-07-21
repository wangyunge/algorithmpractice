class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.res = False
        wordDict = dict(wordDict)
        def _dfs(i):
            if i == len(s):
                self.res = True
            for j in range(i+1, len(s)-1):
                if self.res:
                    break
                if s[i:j+1] in wordDict:
                    _dfs(j+1)
