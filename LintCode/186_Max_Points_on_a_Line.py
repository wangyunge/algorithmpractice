'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example
Given 4 points: (1,2), (3,6), (0,0), (1,3).

The maximum number is 3.
'''
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        res = 0
        for i in xrange(len(points)):
            table = {}
            table['v'] = 1
            same = 0
            for j in xrange(i+1,len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same +=1
                elif points[i].x == points[j].x:
                    table['v'] += 1
                else:
                    slope = 1.0 * (points[i].y - points[j].y)/(points[i].x - points[j].x)
                    if slope in table:
                        table[slope] += 1
                    else:
                        table[slope] = 1
            localMax = max(table.values()) + same
            res = max(res,localMax)
        return res
    def maxPoints(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y: 
                    same += 1
                    continue
                if points[i].x == tx: slope = 'i'
                else:slope = (points[i].y-ty) * 1.0 /(points[i].x-tx)
                if slope not in dic: dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m