'''
Given a linked list, remove the nth node from the end of list and return its head.

 Notice

The minimum number of nodes in list is n.

Have you met this question in a real interview? Yes
Example
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
    	count = 0
    	helper = ListNode(0,head)
        index = helper
        while head:
        	count += 1
        	head = head.next
        	if count > n:
        		index = index.next
        index.next = index.next.next if index.next else index.next
        return helper.next