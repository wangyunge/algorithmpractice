'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        one = two = head

        while two and one:
            one = one.next
            if two.next:
                two = two.next.next
            else:
                return None
            if two == one:
                firstPoint = one
                break
        if one and two:
            two = head
            while two and one:
                if two == one:
                    return one
                else:
                    two = two.next
                    one = one.next
        else:
            return None
