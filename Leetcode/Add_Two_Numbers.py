"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode()
        cur = head 
        while l1 and l2:
            level_res = l1.val + l2.val + carry

            cur.next = ListNode(level_res % 10)
            carry = level_res // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            l = l1 if l1 else l2
            while l:
                level_res = l.val + carry
                cur.next = ListNode(level_res % 10)
                carry = level_res // 10
                cur = cur.next
                l = l.next
        if carry > 0:
            cur.next = ListNode(carry)
        return head.next



            
