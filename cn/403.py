class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:
            return True
        dp = {}
        for i  in  stones:
            dp[i] = set()
        dp[0] = set([1]) # using list 
        for i in stones:
            for last_step in dp[i]:
                if i + last_step  in dp:
                    dp[i+last_step].add(last_step)
                    dp[i+last_step].add(last_step+1)
                    if last_step-1 > 0:
                        dp[i+last_step].add(last_step-1)  # not move backword
        return not len(dp[stones[-1]]) == 0


