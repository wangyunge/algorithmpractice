class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def _bi_ser(x):
            l = 0
            r = len(arr) - 1
            while l <= r:   # Need the equal to tell get l is bigger and r is smaller
                mid = (l+r) // 2
                if arr[mid] < x:
                    l = mid + 1
                elif arr[mid] > x:
                    r = mid - 1
                else:
                    return mid
            return l
        envelopes = sorted(envelopes) # What if they have same width
        arr = []
        for i in range(len(envelopes)):
            if i > 0 and envelopes[i-1][0] == envelopes[i][0]:
                continue
            w, h = envelopes[i]
            pos = _bi_ser(h)
            if pos == len(arr):
                arr.append(h)
            else:
                arr[pos] = h
        return len(arr)

