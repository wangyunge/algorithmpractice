class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def _get_cnt(prefix):
            cur = prefix
            nxt = prefix + 1
            cnt = 0
            while cur <= n:
                cnt += min(nxt, n+1) - cur
                cur *= 10
                nxt *= 10
            return cnt

        def _find(prefix, rest):
            res = []
            base = 1
            bot = 0
            while bot + base * 10 < rest :
                base *= 10
                bot += base

        prefix = 1
        while k > 0:
            cnt = _get_cnt(prefix)
            if cnt < k:
                prefix += 1
                k -= cnt
            elif cnt > k:
                k -= 1
                prefix *= 10




        for i in range(1, 10):
            incre = _get_cnt(i)
            if cnt + incre > k:
                break
            cnt += incre
        _find(i, k-cnt):
        i -= i


