class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                w = i - stack[-1] - 1
                h = heights[idx]
                res = max(res, w*h)
            stack.append(i)
        return res

