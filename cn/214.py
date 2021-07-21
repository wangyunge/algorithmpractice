class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        for i in range(len(s)-1, -1, -1):
            l = 0
            r = i
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    break
            if l >= r:
                break
        head = s[i+1:]
        head = ''.join(head[::-1])
        return head + s

