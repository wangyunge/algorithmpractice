"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = []
        for idx in range(len(s)):
            found = False
            for i in range(len(last)):
                if last[i] == s[idx] :
                    if i+1 < len(last) and last[i+1] < last[i]:
                        for j in range(i, len(last)-1):
                            last[j] = last[j+1]
                        last[-1] = s[idx]
                        found = True
                        break
                    else:
                        found = True
                        continue 
            if not found:
                last.append(s[idx])
        return ''.join(last) 



