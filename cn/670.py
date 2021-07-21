"""
non-negative, float?
max 0 or 1 swaps.

1. brote-force: n^2
2. greedy: maximal on left
put the maximual on the most right to head

"""

from collections import deque
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        pri_que = deque()
        for i in range(len(num)):
            while pri_que and num[pri_que[-1]] <= num[i]:
                # equal means update with the farest one
                pri_que.pop()
            pri_que.append(i)

        for i in range(len(num)):
            while pri_que and  i >= pri_que[0]:
                pri_que.popleft()
            if pri_que and num[i] < num[pri_que[0]]:
                pos = pri_que.popleft()
                num[i], num[pos] = num[pos], num[i]
                break
        return int(''.join(num))


