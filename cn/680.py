class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def _valid(left, right):
            while left < right:
                if s[left] == s[right]:
                    left +=1
                    right -= 1
                else:
                    return False
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        if i >= j:
            return True
        else:
            return _valid(i+1, j) or _valid(i, j-1)

