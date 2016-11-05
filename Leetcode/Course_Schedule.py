'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.res = True
        starters = []
        self.reach = {}
        needPre = set()
        self.allTaken = set()
        for pair in prerequisites:
            if pair[0] in self.reach:
                self.reach[pair[0]].append(pair[1])
            else:
                self.reach[pair[0]] = [pair[1]]
            needPre.add(pair[1])
        for i in xrange(numCourses):
            if i not in needPre:
                starters.append(i)
        for i in starters:
            self.DFS(i,[i])
        return self.res and len(self.allTaken) == numCourses
    def DFS(self,course,taken):
        self.allTaken.add(course)
        if course in self.reach:
            for canTake in self.reach[course]:
                if canTake not in taken:
                    self.DFS(canTake,taken+[canTake])
                else:
                    self.res = False
def main():
    test = [[0,1],[0,2],[1,2]]
    sol = Solution()
    res= sol.canFinish(3,test)
if __name__ == '__main__':
    main()
'''
Notes:
Some courese may need more than one prerequests. Reachability does not equal meeting all the prerequests.
'''