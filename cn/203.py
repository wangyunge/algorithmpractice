# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode()
        prev = dummy
        cur = head
        while cur:
            if cur.val != val:
                prev.next = cur
                prev = cur 
            cur = cur.next 
        prev.next = None
        return dummy.next 