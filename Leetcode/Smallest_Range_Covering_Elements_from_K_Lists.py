"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

 

Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
 

Note:

The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
"""

import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        res =  float('inf')
        idx_list = [0] * len(nums)
        cap = 0
        for arr_idx in range(len(nums)):    # heap initialize
            heapq.heappush(heap, (nums[arr_idx][0], arr_idx))
            cap = max(cap, nums[arr_idx][0])
        while heap:
            bottom , arr_idx = heapq.heappop(heap) # pop 
            res = min(res, cap-bottom)
            in_idx = idx_list[arr_idx]
            if in_idx+1 < len(nums[arr_idx]):  # push new element to heap
                cap = max(cap, nums[arr_idx][in_idx+1])
                heapq.heappush(heap, (nums[arr_idx][in_idx+1], arr_idx))
                idx_list[arr_idx] += 1
            else:
                break   # stop if heap is not full
        return res 





