
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sort_interval = sorted(intervals)
        max_last = float('-inf') 
        res = 0 
        idx = 0
        while idx < len(sort_interval) - 1:
            if sort_interval[idx][0] == sort_interval[idx+1][0]:
                left = idx 
                end = left + 1
                while end < len(sort_interval) and sort_interval[left][0] == sort_interval[end][0]:
                    end += 1
                right = end - 1

                while left < right:
                    sort_interval[left], sort_interval[right] = sort_interval[right], sort_interval[left]
                    left += 1
                    right -= 1
                idx = end
            else:
                idx += 1


        for item in sort_interval:
            if item[1] > max_last:
                res +=1
                max_last = item[1]
        return res
