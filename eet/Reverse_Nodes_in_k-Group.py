"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def _reverse(left, right):
            cur = left
            prev = None
            while cur != right:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

        left = head
        right = head
        cnt = 1
        dummy = ListNode()
        tail = dummy
        while right:

            if cnt == k:
                tmp = right.next
                _reverse(left, right)
                tail.next = right
                tail = left
                left=right=tmp
                cnt = 1
            else:
                right = right.next
                cnt += 1
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self,head,k):
        curr = head
        count = 0
        while curr!=None and count!=k:
            curr = curr.next
            count=count+1
        if count==k:
            curr = self.reverseKGroup(curr,k)
            while count>0:
                temp = head.next
                head.next=curr
                curr = head
                head = temp
                count=count-1
            head = curr
        return head

