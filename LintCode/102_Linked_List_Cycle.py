'''
Given a linked list, determine if it has a cycle in it.
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
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        slow =  head
        fast = head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                return True
        return False 