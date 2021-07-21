
from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = [0]  + A    # prefix summ arry need a 0  as header
        B = A[:]
        for i in range(1, len(A)):
            B[i] = B[i-1] + A[i]
        queue = deque()
        res = len(A)
        for i, item in enumerate(B):
            while queue and B[queue[-1]] > item:
                queue.pop()
            while queue and item - B[queue[0]] > K:
                s  = queue.popleft()
                res = min(res, i-s)
            queue.append(i)
        if res == len(A):
            return -1
        return res






