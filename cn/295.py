import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.q1) == len(self.q2):
            heapq.heappush(self.q1, num)
            mid = heapq.heappop(self.q1)
            heap.heappush(self.q2, -mid)
        elif len(self.q1) < len(self.q2):
            heapq.heappush(self.q2, -num)
            mid = heapq.heappop(self.q2)
            heapq.heappush(self.q1, -mid)


    def findMedian(self):
        """
        :rtype: float
        """
        if not self.q2:
            return
        if len(self.q1) == len(self.q2):
            return (self.q1[0]-self.q2[0]) / 2
        else:
            return -self.q2[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
