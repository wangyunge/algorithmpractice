'''
Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

Have you met this question in a real interview? Yes
Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
'''
z"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        helper = ListNode(0,None)
        index = helper
        while l1 and l2:
            if l1.val <= l2.val:
                index.next = l1
                l1 = l1.next
            else:
                index.next = l2
                l2 = l2.next
            index = index.next
        index.next = l1 if l1 else l2
        return helper.next