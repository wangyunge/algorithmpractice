"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """


        self.head = Node(float("-inf"))
        self.amount = 0


    def addNum(self, num: int) -> None:
        self.amount += 1
        cur = self.head
        last = cur
        while cur:
            if num > cur.val:
                last = cur
                cur = cur.next
            else:
                break
        new_node = Node(num)
        last.next = new_node
        new_node.next = cur

    def findMedian(self) -> float:
        if not self.head.next :
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            return (slow.val + slow.next.val) / 2
        else:
            return slow.next.val


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 388 ms
