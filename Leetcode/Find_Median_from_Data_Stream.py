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


    def addNum(self, num: int) -> None:
        cur = self.head
        last = cur
        while cur:
            if num > cur.val:
                lst = cur
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
