"""
n the
2, 3 , 5
"""

import heapq
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        heap = [2, 3, 5]
        idx = 1
        while idx < n:
            num = heapq.heappop(heap)
            idx += 1
            mul = [2*num, 3*num, 5*num]
            for item in mul:
                if not heap or heap[0] < item:
                    heapq.heappush(heap, item)
        return num
