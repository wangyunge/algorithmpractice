'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head
        table = {}
        helper = RandomListNode(head.label)
        index = helper
        while head:
            if head not in table:
                label = head.label
                newHead = RandomListNode(label)
                table[head] = newHead
            else:
                newHead = table[head]
            index.next = newHead
            index = newHead

            if head.random:
                randomNext = head.random
                if randomNext in table:
                    randomIndex = table[randomNext]
                else:
                    randomIndex = RandomListNode(randomNext.label)
                    table[randomNext] = randomIndex
                index.random = randomIndex

            head = head.next
        return helper.next

