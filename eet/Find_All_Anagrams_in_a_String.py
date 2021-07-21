"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # P duplicate
        L = len(p)
        sort_p = sorted(p)
        res = 0
        for i in range(0, len(s)-L+1) :
            if sort_p == sorted(s[i:i+L]):
                res.append(i)
        return res



class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_table = {}
        L = len(p)
        
        if L > len(s):
            return []
        for char in p:
            p_table.setdefault(char, 0)
            p_table[char] += 1
        cnt = len(p_table)

        for i in range(L):
            if s[i] in p_table:
                p_table[s[i]] -= 1
                
                if p_table[s[i]] == 0:
                    cnt -= 1

        res = [0] if cnt == 0 else []

        for i in range(1, len(s)-L+1):
            if s[i-1] in p_table:
                p_table[s[i-1]] += 1

                if p_table[s[i-1]] == 1:
                    cnt += 1
            if s[i+L-1] in p_table:  
                p_table[s[i+L-1]] -= 1

                if p_table[s[i+L-1]] == 0:
                    cnt -= 1
            if cnt == 0:
                res.append(i)
        return res




