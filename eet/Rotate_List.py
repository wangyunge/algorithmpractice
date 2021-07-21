"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # CC1: mod 0
        # CC2: null head
        if k == 0 or not head:
            return head
        length = 0
        cur  = head
        while cur:
           length += 1 
           cur = cur.next

        if k%length == 0:
            return head 

        new_idx = length - (k % length) + 1

        dummy = ListNode()
        prev = dummy 
        dummy.next = head
        cur = head 
        idx = 0
        while cur :
            idx += 1
            if idx == new_idx:
                dummy.next = cur 
                prev.next =  None
            prev = cur
            cur=cur.next

        prev.next = head if prev != head else None 

        return dummy.next



