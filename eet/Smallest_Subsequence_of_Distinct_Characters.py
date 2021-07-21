"""
Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
'''
!!!!!!!!!!! WHAT IS SUBSEQUENCE !!!!!!!!!!
Clarify the defination before solve the problem.
'''
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        subsequence = [] # (start, end)
        window_table = {}
        left  = 0
        for idx in range(len(s)):
            if s[idx] not in window_table:
                window_table[s[idx]] = idx
            else:
                if window_table[s[idx]] > left:
                    subsequence.append((left, idx-1))
                    left = window_table[s[idx]] + 1
                window_table[s[idx]] = idx
        res = ''

        while subsequence:
            start,end = subsequence.pop()
            cur = s[start,end+1]
            if not res:
                res = cur
            else:
                if _smaller(cur, res):
                    res = cur



        def _smaller(a, b):
            if len(a) < len(b):
                return True
            elif len(a) > len(b):
                return False
            else:
                for idx in range(len(a)):
                    if ord(a[idx]) < ord(b[idx]):
                        return True
                    elif ord(a[idx]) > ord(b[idx]):
                        return False
                return False




        # find all subsequence
        # find the smallest

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # shorter
        # smaller
        last_start = 0
        last_end = len(s) - 1
        smaller = True
        offset = 0
        for idx in range(len(s)):
            # keep table
            if s[idx] not in window_table:
                window_table[s[idx]] = idx
            else:
                if window_table[s[idx]] > left:
                    if smaller:
                        last_start = left
                        last_end = idx-1
                    left = window_table[s[idx]] + 1
                    offset = 0
                window_table[s[idx]] = idx
            # compare last

            if last_start + offset > last_end:
                smaller = False
            else:
                if s[last_start+offset] < s[idx]:
                    smaller = False
            offset += 1
        return s[last_start, last_end+1]

# Let us try to build our answer in greedy way: we take letter by letter and put them into stack: if we have next letter which decreased lexicographical order of string, we remove it from stack and put new letter. However we need to be careful: if we remove some letter from stack and it was the last occurence, then we failed: we can not finish this process. So, we need to do the following:

# Find last_occ: last occurences for each letter in our string
# Initialize our stack either as empty or with symbol, which is less than any letter ('!' in my case), so we do not need to deal with the case of empty stack. Also initialize Visited as empty set.
# Iterate over our string and if we already have symbol in Visited, we just continue.
# Then, we try to remove elements from the top of our stack: we do it, if new symbol is less than previous and also if last occurence of last symbol is more than i: it means that we have removed symbol later in our string, so if we remove it we will not fail to constract full string.
# Append new symbol to our stack and mark it as visited.
# Finally, return string built from our stack.
class Solution:
    def removeDuplicateLetters(self, s):
        last_occ = {c: i for i, c in enumerate(s)}
        stack = ["!"]
        Visited = set()
        
        for i, symbol in enumerate(s):
            if symbol in Visited: continue
            
            while (symbol < stack[-1] and last_occ[stack[-1]] > i):
                Visited.remove(stack.pop())
           
            stack.append(symbol)
            Visited.add(symbol)        
        return "".join(stack)[1:]




