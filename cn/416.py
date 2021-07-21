class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        dp = [[False for _ in range(s+1)] for i in range(len(nums)+1)]
        dp[0][0] = True
        res = False
        for i in range(1, len(nums)+1):
            dp[i][0] = True
            for j in range(1, s+1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j - nums[i-1]] | dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        
        target = total // 2
        if maxNum > target:
            return False
        
        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n - 1][target]

