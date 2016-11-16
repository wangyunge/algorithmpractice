'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

'''
class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        res = 0
        index = 1 
        while index < len(heights):
            left = index
            right = index
            leftH = False
            rightH = False
            while left >= 0:
                if heights[left] <= heights[index]:
                    left -= 1
                else:
                    leftH = True
                    break
            while right < len(heights):
                if heights[right] <= heights[index]:
                    right += 1
                else:
                    rightH = True
                    break
            if leftH and rightH:
                res = res + (right-left-1)*(min(heights[left],heights[right])-heights[index])
            index += 1
        return res
    def trapRainWater(self, heights):
        stack = []
        tmpWater = 0
        for i in xrange(len(heights)):
            if not stack:
                stack.append(i)
            elif heights[stack[-1]] > heights[i]:          
                stack.append(i)
            else:
                while stack and heights[stack[-1]] < heights[i]:
                    bottom = stack.pop()
                    if stack:
                        tmpWater += (min(heights[stack[-1]],heights[i])-bottom)*(i-stack[-1]-1)
                stack.append(i)
        return tmpWater
    def trapRainWater(self,heights):
        left = 0
        right = len(heights)-1
        maxLeft = maxRight = 0
        res = 0
        while left < right:
            if heights[left] <= heights[right]:
                if heights[left] > maxLeft:
                    maxLeft = heights[left]
                else:
                    res += maxLeft - heights[left]
                left += 1
            else:
                if heights[right] > maxRight:
                    maxRight = heights[right]
                else:
                    res += maxRight - heights[right]
                right -= 1
        return res

def main():
    test = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    sol.trapRainWater(test)
if __name__ == '__main__':
    main()