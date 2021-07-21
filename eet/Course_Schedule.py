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


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def _circle_detect(start):
            visited = set()
            stack = [start]
            cur = None
            while cur or stack:
                if cur:
                    if cur in visited:
                        return False
                    visited.add(cur)
                    first = 1
                    for e, s in prerequisites:

                        if s == cur:
                            if first == 1:

                            stack.append(e)
                else:
                    cur = stack.pop()


        for i in range(numCourses):
            if _circle_detect(i):
                return False   
        return True


class Solution:
    """
    use visted value to present the status
    0 for not visited
    1 for still in stack
    2 for finish dfs
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        def DFS(node):
            # Cycle detected.
            if visited[node] == 1:
                return False
            
            # Visit this node, explore neighbors.
            visited[node] = 1
            for nbr in G[node]:
                if visited[nbr] != 2 and not DFS(nbr):
                    return False
            
            # Done visiting node.
            visited[node] = 2
            return True
        
        # Build the graph.
        G = collections.defaultdict(list)
        for postreq, course in prerequisites:
            G[course].append(postreq)
            G[postreq]  # Make sure nodes are made for courses with no postreqs.
        
        visited = [0] * numCourses
        for node in G:
            if not visited[node]:
                if not DFS(node):
                    return False
        return True


def main():
    test = [[0,1],[0,2],[1,2]]
    sol = Solution()
    res= sol.canFinish(3,test)
if __name__ == '__main__':
    main()
'''
Notes:
Some courese may need more than one prerequests. Reachability does not equal meeting all the prerequests.

Method:
1. Topologi sort, keep tracking of not satisfied ingree of each node as Notes mentioned.
2. DFS circle finding. WARNING: In linked list visiting a node twice imply a circle exsitance while in graph a node is visited twice because there are ways from source to this node. Therefore a status need to be recorded if they are in same line. 
'''



def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in xrange(numCourses)]
    visit = [0 for _ in xrange(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in xrange(numCourses):
        if not dfs(i):
            return False
    return True

    # Topology Sort
    def canFinish(self, n, prerequisites):
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n