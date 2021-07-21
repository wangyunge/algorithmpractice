from collections import deque
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def _check(a, b):
            for i in range(len(b)):
                if a == (b[:i] + b[i+1:]):
                    return True
            return False
        reverse_list = {}
        top  = 0
        bottom = float('inf')

        for i, words in enumerate(words):
            l = len(words)
            reverse_list.setdefault(l, [])
            reverse_list[l].append(words)
            top = max(top, l)
            bottom = min(bottom, l)


        cur_stack = reverse_list[bottom]
        bottom += 1
        while bottom <= top:
            for from_word in cur_stack:
                if bottom not in
                for to_word in reverse_list[botoom]:
                    if _check(from_word, to_word)

