'''
Sort a linked list in O(n log n) time using constant space complexity.

Have you met this question in a real interview? Yes
Example
Given 1->3->2->null, sort it to 1->2->3->null.

'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = self.sortList(slow.next)
        slow.next = None
        return self.merge(self.sortList(head),h2)

    def merge(self,leftHead,righHead):
        helper = ListNode(0,None)
        index = helper
        while leftHead and righHead: 
            if leftHead.val <= righHead:
                index.next = leftHead
                leftHead = leftHead.next
            else:
                index.next = righHead
                righHead = righHead.next
            index = index.next
        index.next = leftHead if leftHead else righHead
        return helper.next