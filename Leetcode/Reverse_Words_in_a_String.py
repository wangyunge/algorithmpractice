'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        tmp = ''
        for character in s:
            if character != ' ':
                tmp+=character
            elif tmp!='':
                words.append(tmp)
                tmp = ''
        if tmp!='':
            words.append(tmp)
        words.reverse()
        res = ''
        for word in words:
            res += word + ' '
        res = res.strip()
        return res