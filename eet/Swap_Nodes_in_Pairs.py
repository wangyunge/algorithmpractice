"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

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
        dummy = ListNode()
        even = dummy
        odd = head

        while odd and odd.next:
            even.next = odd.next
            even = odd.next
            tmp_o = even.next
            even.next = odd 
            even = odd
            odd = tmp_o

        even.next = odd

        return dummy.next



