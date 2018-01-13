'''
Given a linked list, swap every two adjacent nodes and return its head.

Have you met this question in a real interview? Yes
Example
Given 1->2->3->4, you should return the list as 2->1->4->3.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return None
        helper = ListNode(0,head)
        left = helper
        right = helper.next
        while right and right.next:
            tmp = right.next.next
            left.next = right.next
            right.next.next = right
            left = right
            right = tmp
            left.next = right
        return helper.next
