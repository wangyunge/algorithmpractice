class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        num = [i+1 for i in range(n)]


        def _next(num):
            # Povit
            # n=2
            for povit in range(len(num)-2, -1 ,-1):
                if num[povit] < num[povit+1]:
                    break
            if povit == 0 and num[povit] > num[povit+1]:
                return num[::-1] # Circle

            for i in range(len(num)-1, povit, -1):
                if num[i] > num[povit]:
                    break
            num[i], num[povit] = num[povit], num[i]
            i = povit + 1
            j = len(num) -1
            while i < j:
                num[i], num[j] = num[j], num[i]
                i += 1
                j -= 1
            return num
        for kth in range(k-1):
            num = _next(num)
        return ''.join(list(map(lambda x: str(x),num)))




