"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = []
        idx = 0
        while 1:
            if idx >= len(strs[0]):
                break
            head = strs[0][idx]
            for i in range(1, len(strs)):
                if idx >= len(strs[i]) or strs[i][idx] != head:
                    break
            res.append(head)
        return ''.join(res)