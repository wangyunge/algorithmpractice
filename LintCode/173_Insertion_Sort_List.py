'''
Sort a linked list using insertion sort.

Have you met this question in a real interview? Yes
Example
Given 1->3->2->0->null, return 0->1->2->3->null.
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
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        helper = ListNode(0)
        while head:
        	insert = head
        	head = head.next
        	slot = helper
        	while slot:
        		if slot.next and insert.val > slot.next.val:
        			slot = slot.next
        		else:
        			tmp = slot.next
        			slot.next = insert
        			insert.next = tmp
        			break
        return helper.next