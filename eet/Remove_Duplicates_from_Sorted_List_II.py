'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Subscribe to see which companies asked this question

Show Tags
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head == None or (head.next != None and head.val == head.next.val):
        #     if head.next.next == None:
        #         return None
        #     else:
        #         head =
        deleting = False
        fakeHead = ListNode(None)
        lastNode = fakeHead
        curr = head
        while curr != None:
            if curr.next != None:
                if curr.val == curr.next.val:
                    deleting = True
                else:
                    if not deleting:
                        lastNode.next = curr
                        lastNode = curr               
                    deleting = False
            else:
                if deleting:
                    lastNode.next = None
                else:
                    lastNode.next = curr
            curr = curr.next
        return fakeHead.next
