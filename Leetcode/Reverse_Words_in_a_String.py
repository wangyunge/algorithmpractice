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


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        spare_spaces = 1 if s[0] == ' ' else 0
        if s[-1] == ' ':
            spare_spaces += 1
        for idx in range(1, len(s)):
            if s[idx] == ' ' and s[idx-1] == ' ':
                spare_spaces += 1
        end  = len(s) - spare_spaces
        left = 0
        store_right = end - 1
        right = len(s) - 1
        while :
            pass
