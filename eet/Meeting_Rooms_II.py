"""
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

 

示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：1

"""

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals)
        res = 0
        heap = [float('-inf')]
        for starti, endi in intervals:
            if starti >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, endi) 
            res = max(len(heap), res)
        return res

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        hours = [0] * 24
        res = 0
        for starti, endi in intervals:
            for idx in range(starti, endi):
                hours[idx-1] += 1
                res = max(res, hours[idx-1])
        return res 


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = soretd(intervals)
        overlap = (0, 0, 0)
        res = 0
        for starti, endi in intervals:  
            if starti < overlap[1]:
                overlap = (max(starti, overlap[0], min(endi, overlap[1]), overlap[2]+1)) # WRONG: dicard the end which may contribute to other intervals
            else:
                overlap = (starti, endi, 1)
            res = max(res, overlap[2])
        return res  


