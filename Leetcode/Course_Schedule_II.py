'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
'''
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in xrange(numCourses)]
        inDegree = [0 for _ in xrange(numCourses)]
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            inDegree[pair[0]] += 1
        import Queue
        queue = Queue.Queue()
        for starter in xrange(numCourses):
            if inDegree[starter] == 0:
                queue.put(starter)
        res = []
        while not queue.empty():
            taking = queue.get()
            res.append(taking)
            for toTake in graph[taking]:
                inDegree[toTake] -= 1
                if inDegree[toTake] == 0:
                    queue.put(toTake)
        if len(res) == numCourses:
            return res
        else:
            return []
