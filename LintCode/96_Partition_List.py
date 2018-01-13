'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Have you met this question in a real interview? Yes
Example
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.
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
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        if not head:
            return None
        helper = ListNode(0)
        helper.next = head
        index = head
        pos = helper
        while index:
            if index.val < x:
                pos = pos.next
                pos.val,index.val = index.val,pos.val 
            index = index.next  
        return helper.next
    def partition(self, head,x):
        if not head:
            return None
        lessHead = ListNode(0)
        greaterHead = ListNode(0)
        index1 = lessHead
        index2 = greaterHead
        while head:
            if head.val < x:
                index1.next = head 
                index1 = index1.next
            else:
                index2.next = head 
                index2 = index2.next
            head = head.next
        index1.next = greaterHead.next
        return lessHead.next
