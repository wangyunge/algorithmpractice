class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    left = stack.pop()
                    dp[i] = i-left+1 + dp[left-1] # 0-1=-1 dp[-1] = 0
        if len(dp) == 0:
            return 0
        return max(dp)

