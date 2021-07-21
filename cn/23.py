# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        headers = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(headers, (lists[i].val, lists[i]))
        dummy = ListNode()
        prev = dummy
        while headers:
            cur, idx = heapq.heappop(headers)
            prev.next = idx
            prev = idx
            to_add = idx.next
            if to_add:
                heapq.heappush(headers, (to_add.val, to_add))

        return dummy.next
