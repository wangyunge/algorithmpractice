class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [[(float('-inf'), float('inf')) for _ in range(len(nums))] for _ in range(3)]
        dp[0][0] = (nums[0], nums[0])
        for i in range(1, len(nums)):
            dp[0][i] = (max(nums[i], dp[0][i-1][0]), min(nums[i], dp[0][i-1][1]))
        for i in range(1, 3):
            for j in range(i, len(nums)) :
                tmp_max = max(dp[i-1][j-1][0] * nums[j], dp[i-1][j-1][1] * nums[j])
                tmp_min = min(dp[i-1][j-1][0] * nums[j], dp[i-1][j-1][1] * nums[j])
                tmp_max = max(dp[i][j-1][0], tmp_max)
                tmp_min = min(dp[i][j-1][1], tmp_min)
                dp[i][j] = (tmp_max, tmp_min)
        return dp[-1][-1][0]