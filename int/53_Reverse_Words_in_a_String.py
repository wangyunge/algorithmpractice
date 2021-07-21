'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Have you met this question in a real interview? Yes
Clarification
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''
class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        wordList = []
        pack = ''
        for character in s:
            if character == ' ':
                if pack:
                    wordList.append(pack)
                    pack = ''
            else:
                pack = pack + character
        if pack:
            wordList.append(pack)
        wordList.reverse()
        res = ' '.join(wordList)
        return res
'''
"join" method applies to string not list.
Be careful about the end of the iteration. Don't forget to add the last element.
'''