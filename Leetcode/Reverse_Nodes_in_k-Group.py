"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def _reverse_k(head):
            if not head.next:
                return head
            prev = head
            head = head.next 
            cnt = 2
            while head and cnt <= k:
                cnt += 1
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return prev
        if not head or not head.next:
            return head
        res = None
        while head.next:
            cur_head = head.next
            head = _reverse_k(head.next)
            if res is None:
                res = head
            else:
                prev_head.next = head
            prev_head = cur_head



