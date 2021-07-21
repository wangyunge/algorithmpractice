class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stack = []
        if x <0:
            return False
        if x == 0:
            return True 
        x = abs(x)
        while x != 0:
            stack.append(x % 10)
            x = x // 10
        left = 0
        right = len(stack) - 1
        while left < right:
            if stack[left] != stack[right]:
                return False 
            left += 1
            right -= 1
        return True 

