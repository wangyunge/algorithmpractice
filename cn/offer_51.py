class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0
        def _merge(a, b):
            i = 0
            j = 0
            c = []
            while i < len(a) and j < len(b):
                if a[i] > b[j]:
                    self.res += len(b) - j
                    c.append(a[i])
                    i += 1
                else:
                    c.append(b[j])
                    j += 1
            while i < len(a):
                c.append(a[i])
                i += 1
            while j < len(b):
                c.append(b[j])
                j += 1
            return c
        def _merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            return _merge(_merge_sort(arr[:mid]), _merge_sort(arr[mid:]))
        _merge_sort(nums)
        return self.res



