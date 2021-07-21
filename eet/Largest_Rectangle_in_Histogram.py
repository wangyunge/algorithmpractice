'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

Subscribe to see which companies asked this question
'''

# #1 brute force
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        highest = 0
        for L in xrange(0,len(heights)-1):
            lowest = heights[L]
            for R in xrange(L,len(heights)-1):
                if heights[R] < lowest:
                    lowest = heights[R]
                if (R-L+1)*lowest > highest:
                    highest = (R-L+1)*lowest
        return highest

# #2 when each bar is a the height(lowest around)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return
        res = 0
        for lowest_idx in range(len(heights)):
            left = right = lowest_idx
            while left >= 0 and heights[left] >= heights[lowest_idx]:
                left -= 1
            while right <= len(heights)-1 and heights[right] >= heights[lowest_idx]:
                right += 1
            res = max(res, heights[lowest_idx]*(right-left-1)) 

        return res

# #3 let stack take care of position, what is "around"
class Solution(object):
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        res = 0 
        heights.append(-1)
        stack = [-1, 0]
        for idx in range(1, len(heights)):
            while heights[stack[-1]] > heights[idx]:
                cur_height = heights[stack.pop()]
                res = max(res,cur_height*(idx - stack[-1] -1))
            stack.append(idx)
        return res

