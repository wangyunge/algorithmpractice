"""
在由 2D 网格表示的校园里有 n 位工人（worker）和 m 辆自行车（bike），n <= m。所有工人和自行车的位置都用网格上的 2D 坐标表示。

我们需要为每位工人分配一辆自行车。在所有可用的自行车和工人中，我们选取彼此之间曼哈顿距离最短的工人自行车对  (worker, bike) ，并将其中的自行车分配給工人。如果有多个 (worker, bike) 对之间的曼哈顿距离相同，那么我们选择工人索引最小的那对。类似地，如果有多种不同的分配方法，则选择自行车索引最小的一对。不断重复这一过程，直到所有工人都分配到自行车为止。

给定两点 p1 和 p2 之间的曼哈顿距离为 Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|。

返回长度为 n 的向量 ans，其中 a[i] 是第 i 位工人分配到的自行车的索引（从 0 开始）。

输入：workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
输出：[1,0]
解释：
工人 1 分配到自行车 0，因为他们最接近且不存在冲突，工人 0 分配到自行车 1 。所以输出是 [1,0]。

输入：workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
输出：[0,2,1]
解释：
工人 0 首先分配到自行车 0 。工人 1 和工人 2 与自行车 2 距离相同，因此工人 1 分配到自行车 2，工人 2 将分配到自行车 1 。因此输出为 [0,2,1]。

"""



import heapq
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        cnt = 0
        res = [-1 for _ in range(len(workers))]
        heap = []
        packed = set()
        def _distance(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        for i, bike in enumerate(bikes):
            for j, worker in enumerate(workers):
                    heapq.heappush(heap, (_distance(worker, bike), i, j))
        
        while cnt < len(workers)  :
            _, i, j = heapq.heappop(heap)
            if res[j] == -1 and i not in packed:
                res[j] = i
                cnt += 1
                packed.add(i)
        return res 



