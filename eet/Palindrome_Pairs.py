"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def _check(word_a, word_b):

            l = 0
            r = len(word_a) + len(word_b)  
            while l < r:
                a = word_a[l] if l < len(word_a) else word_b[l-len(word_a)]
                b = word_a[r-len(word_a)]  if r >= len(word_a) else word_b[r] 
                if a != b:
                    return False 
                l += 1
                r -= 1
            return True
        res = []
        for i in range(len(words)):
            for j in range(i, len(words)):
                if _check(words[i], word[j]):
                    res.append([i, j])
                if _check(words[j], word[i]):
                    res.append([j, i])
        return res





