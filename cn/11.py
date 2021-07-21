class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            w = r-l-1
            res = max(res, w*min(height[l], height[r]))
            if height[r] < height[l]:
                r -= 1
            elif height[r] >= height[l]:
                l += 1
        return res
