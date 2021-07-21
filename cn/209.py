from collections import deque
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        queue = deque()
        cul_sum = [0]
        for item in nums:
            cul_sum.append(cul_sum[-1] + item)

        res = len(cul_sum)
        for i in range(len(cul_sum)):
            while queue and cul_sum[queue[-1]] > cul_sum[i]:
                queue.pop()
            queue.append(i)
            while cul_sum[queue[-1]] - cul_sum[queue[0]]  >= target:
                head = queue.popleft()
                res = min(res, queue[-1]-head)


        res = 0 if res == len(cul_sum) else res 
        return res


