class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def _is_par(i, j):
            if i==j:
                return True
            else:
                if s[i] == s[j]:
                    if i+1<j-1:
                        spd_up_dp[i][j] = spd_up_dp[i+1][j-1]
                    else:
                        spd_up_dp[i][j] = True
                return spd_up_dp[i][j]
        spd_up_dp = [[True if i==j else False for j in range(len(s))] for i in range(len(s))]
        dp = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if _is_par(j, i):
                    for item in dp[j-1]:
                        dp[i].append(item+[s[j:i+1]])
        return dp[-1]
