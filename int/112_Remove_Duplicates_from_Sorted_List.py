'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Have you met this question in a real interview? Yes
Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        helper = ListNode(None,None)
        build = helper
        explore = head
        lastVal = None
        while explore:
            if explore.val != lastVal:
                build.next = explore
                build = build.next
            lastVal = build.val
            explore = explore.next
        build.next = None
        return helper.next