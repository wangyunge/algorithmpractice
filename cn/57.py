class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        add = False
        s = newInterval[0]
        e = newInterval[1]
        for item in intervals:
            if item[1] < s:
                res.append(item)
            elif item[0] > e:
                if not add:
                    res.append([s, e])
                    add = True
                res.append(item)
            else:
                s = min(item[0], s)
                e = max(item[1], e)
        if not add:
            res.append([s, e])
            add = True

        return res

"""
1. trigger of append res
"""
