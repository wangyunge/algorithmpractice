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
        dummy= RandomListNode()
        dummy.next = head
        cur = head

        while cur:
            new_node = RandomListNode(cur.label)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        cur = head
        prev = dummy
        while cur:
            prev.next = cur.next
            prev = cur.next
            prev.random = cur.random.next
            cur.next = prev.next
            cur = prev.next
        return dummy.next





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


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return head

        pointer = head
        while pointer:
            tmp = pointer.next
            pointer.next = RandomListNode(pointer.label)
            pointer.next.next = tmp
            pointer = tmp

        pointer = head
        res = head.next
        copy_pointer = res
        while pointer:
            copy_pointer.random = pointer.random.next
            pointer.next = copy_pointer.next
            pointer = copy_pointer.next
            copy_pointer.next = pointer.next

        return res


