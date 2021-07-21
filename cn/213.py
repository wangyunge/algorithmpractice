class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0
        dp = [money for money in nums[:-1]]
        if len(dp) > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(dp)):
            rob = dp[i-2] + nums[i]
            not_rob = dp[i-1]
            dp[i] = max(rob, not_rob)
        c1 = dp[-1]
        dp = [nums[i+1] for i in range(len(nums)-1)]
        if len(dp) > 1:
            dp[1] = max(nums[1], nums[2])
        for i in range(2, len(dp)):
            rob = dp[i-2] + nums[i+1]
            not_rob = dp[i-1]
            dp[i] = max(rob, not_rob)
        c2 = dp[-1]
        return max(c1, c2)


