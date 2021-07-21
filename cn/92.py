# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # Circle
        # more than one time
        def _rev(start):
            cur = start
            prev = None
            while cur and cur.val != right:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            if cur:
                next_head = cur.next
                cur.next = prev
                prev = cur
                return start, prev, next_head
            else:
                return start, prev, None

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if cur.val == left:
                a, b, c = _rev(cur)
                prev.next = b
                prev = a
                cur = c
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
        return dummy.next
