# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def _swap(a, b):
            if b:
                c = b.next
                b.next = a
                a.next = None
                return a, b, c
            else:
                return a, a, None
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            a, b, c = _swap(cur, cur.next)
            prev.next = b
            prev = a
            cur = c
        return dummy.next
