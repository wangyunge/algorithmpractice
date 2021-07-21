'''
Sort a linked list using insertion sort.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(float("-inf"))
        while head:
            curr = head
            head = head.next
            L = newHead
            while L:
                if L.next:
                    if curr.val <= L.next.val:
                        tmp = L.next
                        L.next = curr
                        curr.next = tmp
                        break
                else:
                    L.next = curr
                    curr.next = None
                    break
                L = L.next
        return newHead.next

