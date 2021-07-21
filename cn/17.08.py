class Solution(object):
    def bestSeqAtIndex(self, height, weight):
        """
        :type height: List[int]
        :type weight: List[int]
        :rtype: int
        """
        person = []
        for i in range(len(height)):
            person.append((height[i], weight[i]))
        person = sorted(person)
        dp = [1 for _ in range(len(height))]
        for i in range(1, len(height)):
            for j in range(i):
                if person[j][1] < person[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
"""
Notes:
1. binary search as LIS
2. sort reversely when height equals
"""
