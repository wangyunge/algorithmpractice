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

        # Reverse whole string
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1 
            righ -= 1

        # Revers words
        left = None
        for idx in range(0, len(s)):
            if not left and  s[idx] != ' ':
                left=idx
            elif left and s[idx] == ' ':
                right = idx - 1

                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left +=1 
                    righ -= 1
                left = None

        # Clean spaces
        pos = 0
        last = ' '
        for idx in range(0, len(s)):
            if last == ' ' and s[idx] == ' ':
                continue
            else:
                s[pos] = s[idx]
                last = s[idx]
                pos += 1
        return s[:pos]


