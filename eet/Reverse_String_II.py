"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = 0
        right = k - 1
        left = 0
        if k == 0:
            return s
        s = [ch for ch in s]
        while right < len(s):
            while  left < right :
                s[left], s[right] = s[right], s[left]
                left += 1 
                right -= 1
            n += 1
            left = (2 * n ) * k
            right = (2 * n  + 1) * k - 1
        if left < len(s) and right >= len(s):
            right = len(s) - 1
            while  left < right :
                s[left], s[right] = s[right], s[left]
                left += 1 
                right -= 1
        return ''.join(s)

def main():


if __name__ == '__main__':
    main()
