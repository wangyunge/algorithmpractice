'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        for rowNum in xrange(1,len(triangle)):
            for colNum in xrange(0,rowNum+1):
                tmp = triangle[rowNum][colNum]
                if colNum ==0:
                    triangle[rowNum][colNum] = triangle[rowNum-1][colNum] + tmp
                elif colNum == rowNum:
                    triangle[rowNum][colNum] = triangle[rowNum-1][colNum-1] +tmp
                else:
                    triangle[rowNum][colNum] = min(triangle[rowNum-1][colNum],triangle[rowNum-1][colNum-1]) + tmp
        return min(triangle[len(triangle)-1])
