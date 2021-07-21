'''
Given an array of strings, return all groups of strings that are anagrams.

 Notice

All inputs will be in lower-case

Have you met this question in a real interview? Yes
Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].
'''
class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        table = {}
        res = []
        for word in strs:
            setOfWord = set(word)
            if setOfWord not in table:
                table[setOfWord] = word
            else:
                res.append(word)
        return res
