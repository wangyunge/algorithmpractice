'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

 Notice

You may not slant the container.

Have you met this question in a real interview? Yes
Example
Given [1,3,2], the max area of the container is 2.
'''
class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        if not heights:
            return 0
        left = 0
        right = len(heights)-1
        res = min(heights[left],heights[right])*(right-left)
        while left < right:
            res = max(min(heights[left],heights[right])*(right-left),res)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return res
