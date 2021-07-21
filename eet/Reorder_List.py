'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        stack = []
        cur = head

        while cur:
            stack.append(cur)
        left = head
        right = None

        while left and stack:
            right = stack.pop()
            tmp = left.next
            if left == right:
                break
            else:
                left.next = right
            if right == tmp:
                break
            else:
                right.next = tmp
            left = tmp

        right.next = None # Close the tail is CRITICAL !!!!
        return head
"""
Note:
Close the tail of the list
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head:
            stack = []
            index = head
            while index:
                stack.append(index)
                index = index.next
            L = head
            R = stack.pop()
            while L != R:
                tmp = L.next
                if L.next != R:
                    L.next = R
                else:
                    break
                R.next = tmp
                L = tmp
                R = stack.pop()
            R.next = None
