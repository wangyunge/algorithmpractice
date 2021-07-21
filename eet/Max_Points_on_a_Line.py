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
        def _gcd(a, b):
            """
            Greatest common divisor
            """
            if b == 0:
                return a 
            return _gcd(b, a%b) 

        def _slop(i, j):
            if i.x==j.x:
                return 'ver'
            else:
                y_diff = i.y-j.y
                x_diff = i.x-j.x

                slop = _gcd(y_diff, x_diff) 
                return str(slop)
             
        for i in range(len(points)):
            table = {}
            dupl = 1
            for j in range(i, len(points)):
                if i.x==j.x and i.y==j.y:
                    dupl += 1
                else:
                    slop = _slop(i, j)
                    table.setdefault(slop, 0)
                    table[slop] += 1
                res = max(res, max(table.values())+dupl+1)
        return res









