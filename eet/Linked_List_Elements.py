'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        helper =  ListNode(None)
        helper.next = head
        index_1 = helper
        index_2 = helper.next
        while index_2:
            if index_2.val == val:
                index_1.next = index_2.next
                index_2 = index_2.next
            else:
                index_1,index_2 = index_2,index_2.next
        return helper.next