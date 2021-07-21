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
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        res = []
        while s1 and s2:
            a1 = s1.pop()
            a2 = s2.pop()
            a3 = a1+a2+carry
            res.append(a3 % 10)
            carry = a3 // 10
        rest = s1 if s1 else s2

        while rest:
            a1 = rest.pop()
            a3 = a1+carry
            res.append(a3 % 10)
            carry = a3 // 10
        if carry > 0:
            res.append(carry)
        dummy = ListNode(0)
        cur = dummy
        while res:
            cur.next = ListNode(res.pop())
            cur = cur.next
        return dummy.next

