'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

Subscribe to see which companies asked this question
'''
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