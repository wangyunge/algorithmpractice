"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def _merge_two(a, b):
            fake_head = ListNode(0)
            head = fake_head
            while a and b :
                if a.val <= b.val:
                    head.next = a 
                    head = a 
                    a = a.next
                else:
                    head.next = b 
                    head = b 
                    b = b.next
            if a:
                head.next = a 
            if b:
                head.next = b
            return fake_head.next

        def _merge_sort(arr):
            if len(arr) == 1:
                return arr[0]
            mid = len(arr) // 2
            left = _merge_sort(arr[:mid])
            right = _merge_sort(arr[mid:])
            return _merge_two(left, right)

        return _merge_sort(lists)



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self,lists):
        if not lists:
            return []
        heap = []
        for headers in lists:
            if headers:
                heapq.heappush(heap,(headers.val,headers))
        if not heap:
            return []
        (value,head) = heapq.heappop(heap)
        operator = head
        if head.next:
            heapq.heappush(heap,(head.next.val,head.next))

        while heap:
            (value,poped) = heapq.heappop(heap)
            operator.next = poped
            operator = operator.next
            if poped.next:
                heapq.heappush(heap,(poped.next.val,poped.next))
        return head
