class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if dividend * divisor > 0 else -1
        divisor = abs(divisor)
        dividend = abs(dividend)
        def _sub(res):
            x = divisor
            if res < divisor:
                return 0
            ans = 1
            while 2 * x <= res:
                x = 2 * x
                ans = 2 * ans
            return ans + _sub(res-x)
        return _sub(dividend)


