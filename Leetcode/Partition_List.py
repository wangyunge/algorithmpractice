'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

Subscribe to see which companies asked this question
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        H1 = ListNode(None)
        L = H1
        H2 = ListNode(None)
        R = H2
        curr = head
        H3 = ListNode(None)
        M = H3
        while curr:
            if curr.val < x:
                L.next = curr
                L = curr
            elif curr.val > x:
                R.next = curr
                R = curr
            else:
                M.next = curr
                M = curr
            curr = curr.next
        if H3.next:
            L.next = H3.next
            M.next = H2.next if H2.next else None
        else:
            L.next = H2.next if H2.next else None
        R.next = None
        return H1.next