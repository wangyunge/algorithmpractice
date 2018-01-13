'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Have you met this question in a real interview? Yes
Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        if not head:
            return head
        length = 1
        index = head
        while index.next:
            length += 1
            index = index.next
        k = k % length
        index.next = head
        helper = ListNode(0,head)
        index = helper
        step = 0
        while step < length-k:
            index = index.next
            step += 1
        helper.next = index.next
        index.next = None
        return helper.next
