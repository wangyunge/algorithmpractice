"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
"""



class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s) 
        table = {}
        for idx in range(len(s)):
            last_id, cnt = table.get(s[idx], (len(s), 0))
            table[s[idx]] = (min(last_id, idx), cnt+1)

        for last_id, cnt in table.keys():
            if cnt == 1:
                res = min(res, last_id)
        if res == len(s):
            return -1
        else:
            return res
