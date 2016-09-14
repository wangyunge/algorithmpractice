'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        one  =  head
        if head and head.next:
            two =  head.next
        else:
            return False
        while two and one:
            if two == one:
                return True
            one = one.next
            if two.next:
                two = two.next.next
            else:
                return False
        return False