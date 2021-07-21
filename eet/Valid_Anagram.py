"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table ={}
        for item in s:
            table.setdefault(item, 0)
            table[item] += 1
        for item in t:
            if item in table:
                table[item] -= 1
            else:
                return False
        for _, value in table.items():
            if value > 0:
                return False 
        return True
