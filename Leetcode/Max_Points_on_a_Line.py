'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def slop_cal(a,b):
            if a.y==b.y and a.x==b.x:
                return 'root'
            slop = (a.y-b.y)/(a.x-b.x) if a.x != b.x else float('inf')
            return slop
        for idx1 in range(len(points)):
            slop_table = {'root':0}
            for idx2 in range(idx1, len(points)):
                slop = slop_cal(points[idx1], points[idx2])
                slop_table.setdefaul(slop, 0)
                slop_table[slop] += 1
            res = max(res, max(slop_table.values()) + slop_table['root'])



