class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        tail = 0
        res = 0
        for i, char in enumerate(s):
            if char in table and  table[char] >= tail:
                tail = table[char] + 1
            table[char] = i
            res = max(res, i - tail + 1)
        return res



