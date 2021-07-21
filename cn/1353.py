class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if not events:
            return 0


        dp = [1 for _ in range(len(events))]
        for i in range(1, len(events)):
            for j in range(i-1, -1 , -1):
                if events[i][0] >= events[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                else:
                    break
        return max(dp)
