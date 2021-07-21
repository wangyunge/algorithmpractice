"""
x, y -> z
a1: fill x ,y
a2: emptyfy 0, 0
a3: transfer  x-y, y-x ,
"""

class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        x = max(jug1Capacity, jug2Capacity)
        y = min(jug1Capacity, jug2Capacity)
        visted = {}
        if targetCapacity > x + y:
            return False
        def _dfs(inx, iny):
            if inx+iny == targetCapacity:
                return True
            visited.add((inx, iny))
            res = False
            # Emptify
            if inx > 0 and not res:
                if (0, iny) not in visited:
                    res = res | _dfs(0, iny)
            if iny > 0 and not res:
                if (inx, 0) not in visited:
                    res = res | _dfs(inx, 0)
            if inx < x and not res:
                res = res | _dfs(x, iny)
            if iny < y and not res:
                res =  res | _dfs(inx, y)
            # To x
            if inx+iny < x and not res:
                res = res | _dfs(inx+iny, 0)
            if inx + iny > x and not res:
                res =  res  | _dfs(x, inx+iny-x)
            #To y
            if inx+iny < y and not res:
                res = res | _dfs(0, inx+iny)
            if inx + iny > y and not res:
                res = res | _dfs(inx+iny-y, y)
            return res
        return _dfs(0, 0)
