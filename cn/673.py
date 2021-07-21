class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[1, 1] for _ in range(len(nums))] # [count, length]
        max_len = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][1] + 1 > dp[i][1]:
                        dp[i][0] = dp[j][0]
                    elif dp[j][1] + 1 == dp[i][1]:
                        dp[i][0] += dp[j][0]
                    dp[i][1] = max(dp[j][1]+1, dp[i][1])
                    max_len = max(max_len, dp[i][1])
        res = 0
        for i in range(len(dp)):
            if dp[i][1] == max_len:
                res += dp[i][0]
        return res



