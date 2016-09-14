'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list. 
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        table = {}
        if not head:
            return None
        resHead = RandomListNode(head.label)
        table[head] = resHead
        H2 = resHead
        while head:
            if head.next:
                if head.next in table:
                    H2.next = table[head.next]
                else:
                    H2.next = RandomListNode(head.next.label)
                    table[head.next] = H2.next
            if head.random:
                if head.random in table:
                    H2.random = table[head.random]
                else:
                    H2.random = RandomListNode(head.random.label)
                    table[head.random] = H2.random

            head = head.next
            H2 = H2.next
        return resHead