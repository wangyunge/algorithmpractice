class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [1]
        idxs = [0] * len(primes)
        for j in range(1, n):
            tmp_list= [dp[idxs[i]] * primes[i] for i in range(len(primes))]
            pick = min(tmp_list)
            dp.append(pick)
            for i in range(len(primes)):
                if pick == tmp_list[i]:
                    idxs[i] += 1
        return dp[-1]

