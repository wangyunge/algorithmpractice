class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def _gcd(m, n):
            a = max(m, n)
            b = min(m, n)
            c = a % b
            if c == 0:
                return b
            else:
                return _gcd(b, c)
        def _slop(p1, p2):
            if p1[0] == p2[0]:
                return (0, 1)
            elif p1[1] == p2[1]:
                return (1, 0)
            else:
                delta_x = p1[0]-p2[0]
                delta_y = p1[1]-p2[1]
                sign = 1 if delta_y * delta_x > 0 else -1

                gcd = _gcd(abs(delta_x), abs(delta_y))
                return (sign * abs(delta_x) / gcd, abs(delta_y) / gcd)
        res = 0
        for i in range(len(points)):
            table = {}
            res = max(res, 1)
            for j in range(i+1, len(points)):
                slop = _slop(points[i], points[j])
                table.setdefault(slop, 1)
                table[slop] += 1
                res = max(res, table[slop])
        return res
