from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not beginWord:
            return []

        def _children(cur_word):
            children = []
            for i in range(len(cur_word)):
                for j in range(26):
                    concat_word = cur_word[:i] +
            return children
        def _children(cur_word):
            children = []
            for word in wordList:
                if _dist(cur_word, word) == 1 and word not in visited:
                    children.append(word)
            return children
        def _dist(a, b):
            d = 0
            for i in range(len(a)):
                if a[i] != b[b]:
                    d += 1
                id d > 1:
                    break
            return d

        queue = deque()
        queue.append([beginWord])
        res_l = float('inf')
        while queue:
            cur_path = queue.popleft()
            if len(cur_path) > res_l:
                continue
            if cur_path[-1] == endWord:
                res.append(cur_path)
                res_l = min(res_l, len(cur_path))
            for word in _children(cur_word):
                queue.append(cur_path + [word])
        return res



