'''
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln

reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Have you met this question in a real interview? Yes
Example
Given 1->2->3->4->null, reorder it to 1->4->2->3->null.

'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves
def _splitList(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        fast = fast.next

    middle = slow.next
    slow.next = None

    return head, middle

# Reverses in place a list.
# @return Returns the head of the new reversed list
def _reverseList(head):

  last = None
  currentNode = head

  while currentNode:
    nextNode = currentNode.next
    currentNode.next = last
    last = currentNode
    currentNode = nextNode

  return last

# Merges in place two lists
# @return The newly merged list.
def _mergeLists(a, b):

    tail = a
    head = a

    a = a.next
    while b:
        tail.next = b
        tail = tail.next
        b = b.next
        if a:
            a, b = b, a
            
    return head


class Solution:

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if not head or not head.next:
            return

        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)