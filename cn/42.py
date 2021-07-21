class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                bottom = height[stack.pop()]
                if stack:
                    brick = min(height[stack[-1]], height[i])
                    w = i - stack[-1] - 1
                    res += (brick-bottom) * w
            stack.append(i)
        return res



