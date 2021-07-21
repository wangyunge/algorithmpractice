class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        need = {} # count the degree
        as_pre = {} # witch course it contributes to
        for cur, pre in prerequisites:
            need.setdefault(cur, 0)
            need[cur] += 1
            as_pre.setdefault(pre, [])
            as_pre[pre].append(cur)
        nxt = []
        for i in range(numCourses):
            if i not in need:
                nxt.append(i)
                numCourses -= 1
        while nxt:
            cur = nxt.pop()
            ctb_list = as_pre.get(cur, [])
            for ctb in  ctb_list:
                if ctb in need and need[ctb] > 0:
                    need[ctb] -= 1
                    if need[ctb] == 0:
                        nxt.append(ctb)
                        numCourses -= 1
        return numCourses == 0


