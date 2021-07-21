import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _check(x):
            bounder = math.sqrt(x)
            for item in res:
                if x % item == 0:
                    return False
                if item > bounder:
                    return True 
            return True 
        res = []
        for number in range(2, n):
            if _check(number):
                res.append(number)
        return len(res)

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime_arr = [1 for _ in range(n+1)]
        res = 0
        for idx in range(2, n+1):
            if prime_arr[idx] == 1:
                res += 1

                mul = idx
                pos = mul * idx
                while pos <= n:
                    prime_arr[pos] = 0
                    mul += 1
                    pos = mul * idx
        return res

