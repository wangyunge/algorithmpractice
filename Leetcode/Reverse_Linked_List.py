'''
Reverse a singly linked list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        index = head.next
        while index:
            cur = index
            index = index.next
            cur.next = head
            head = cur
        return head
class Solution:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev