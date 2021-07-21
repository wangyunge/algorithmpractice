class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)
        while i < j:
            if not s[i].isdigit() or not s[i].isalpha():
                i +=1
                continue
            if not s[j].isdigit() or not s[j].isalpha():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True 