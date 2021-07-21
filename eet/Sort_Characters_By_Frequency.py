"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = []
        l = [[]] * le(s)
        for char in s:
            table.setdefaul(char, 0)
            table[char] += 1
        for k, v in table.items():
            l[v].append(k)
        res = []
        for idx in range(len(s)-1, -1, -1):
            for item in l[idx]:
                res.append(item)
        return res


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        # Bucke sort
