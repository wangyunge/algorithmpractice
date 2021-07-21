from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        res = []
        queue = deque()
        for idx in range(k-1):
            while queue and nums[queue[-1]] < nums[idx]:
                queue.pop()
            queue.append(idx)
        for idx in range(k-1, len(nums)):
            while queue and nums[queue[-1]] < nums[idx]:
                queue.pop()
            queue.append(idx)
            while queue and idx - queue[0] >= k:
                queue.leftpop()
            res.append(nums[queue[0]])
        return res 


"""
[3, 2, 3] ,4, 4
3 [ 2, 3  ,4], 4
"""

