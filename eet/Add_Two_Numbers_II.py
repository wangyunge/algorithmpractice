"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
        def _reverse(l1):
            prev = None
            while l1:
                tmp = l1.next
                l1.next = prev
                prev = l1
                l1 = tmp
            return prev
        l1 = _reverse(l1)
        l2 = _reverse(l2)
        carry = 0
        while l1 and l2:
            carry = (l1.val+l2.val) // 10
            
if __name__ == '__main__':
    main()