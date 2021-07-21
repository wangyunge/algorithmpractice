"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table = {}
        capacity = 0
        rr, rl = 0 ,len(s) - 1
        for char in t:
            table.setdefalt(char, 0)
            table[char] += 1
            capacity += 1
        left = -1
        for right in range(len(s)):
            if s[right] in table:
                table[s[right]] -= 1
                if table[s[right]] >= 0:
                    capacity -= 1
            while capacity == 0 and  left <= right:
                if right - left < rr - rl:
                    rr, rl = right, left
                left += 1
                if s[left] in table:
                    table[s[left]] += 1
                    if table[s[left]] > 0:
                        capacity += 1
        return s[rl:rr+1]


























from collections import deque
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table = {}
        for char in t:
            table[char] = 0
        missing = len(t)
        left = 0
        for right in range(len(s)):
            if s[right] not in table:
                continue
            table[s[right]] += 1
            while left <= right:
                if s[right] not in table:
                    left += 1
                    continue
                if table[s[left]] > 1:
                    table[s[left]] -= 1
                    left += 1
                else:
                    break

            res = min(res, right - left + 1)
        return res



# The current window is s[i:j] and the result window is s[I:J]. In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing. In the loop, first add the new character to the window. Then, if nothing is missing, remove as much as possible from the window start and then update the result.

def minWindow(self, s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]
