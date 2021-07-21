class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def _next(x):
            res = 0
            while x > 0:
                res += pow(x % 10, 2)
                x = x // 10
            return res
        table = set()
        while True:
            n = _next(n)
            if n in table:
                break
            table.add(n)
        return n == 1


