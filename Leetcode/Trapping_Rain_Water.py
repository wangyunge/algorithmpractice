"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height: List[int]) -> int:


class Solution(object):
    def trap(self,height):
        water = 0
        barral = []
        for curr in xrange(len(height)):
            if curr ==0:
                barral.append(curr)
            else:
                if height[barral[-1]]>height[curr]:
                    barral.append(curr)
                else:
                    eq=False
                    bottom = 1
                    while barral and height[barral[-1]]<=height[curr]:
                        if height[barral[-1]]==height[curr]: eq=True
                        poped = barral.pop()
                        water = water+(curr-poped-1)*(height[poped]-height[bottom])
                        bottom = poped
                        
                    if barral and not eq:
                        water = water+(curr- barral[-1] -1)*(height[curr]-height[bottom])
                    barral.append(curr)
        return water 