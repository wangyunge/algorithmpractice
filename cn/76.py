class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        status = {}
        distinct = 0
        res = ''
        max_len = len(s)
        for item in t:
            if item in status:
                status[item] += 1
            else:
                status[item] = 1
                distinct += 1
        right = 0
        left = 0

        for right in range(len(s)):
            if s[right] in status:
                status[s[right]] -= 1
                if status[s[right]] == 0:
                    distinct -= 1
                while distinct == 0:
                    if right-left < max_len:
                        res = s[left:right+1]
                        max_len = right-left
                    if s[left] in status:
                        status[s[left]] += 1
                        if status[s[left]] == 1:
                            distinct += 1
                    left += 1
        return res



