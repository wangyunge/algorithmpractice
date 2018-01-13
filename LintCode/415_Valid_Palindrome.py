'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 Notice

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Have you met this question in a real interview? Yes
Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.
'''
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        s2 = ''
        for chara in s:
        	if chara.isalpha() or chara.isdigit():
        		s2 += chara.lower()
        left = 0
        right = len(s2)-1
        while left < right:
        	if s2[left] == s2[right]:
        		left += 1
        		right -= 1
        	else:
        		return False
        return True
