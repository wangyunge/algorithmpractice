'''
Given k strings, find the longest common prefix (LCP).

Have you met this question in a real interview? Yes
Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"

For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"
'''
class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        index = 0
        res = ''
        while True:
            if index >= len(strs[0]):
                return res
            thisChar = strs[0][index]
            for string in strs:
                if index >= len(string):
                    return res
                if string[index] != thisChar:
                    return res
            res += thisChar
            index += 1