class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [money for money in nums] # max I can get at up to this house
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            rob = dp[i-2] + nums[i]
            not_rob = dp[i-1]
            dp[i] = max(rob, not_rob)
        return dp[-1]


