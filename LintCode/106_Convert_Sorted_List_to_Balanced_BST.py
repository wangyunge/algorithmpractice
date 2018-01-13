'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Have you met this question in a real interview? Yes
Example
               2
1->2->3  =>   / \
             1   3
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        index = head.next
        mid = head
        while index:
            if index.next and index.next.next:
                index = index.next.next
            else:
                break
            mid = mid.next
        root = TreeNode(mid.next.val)
        right = mid.next.next
        mid.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root

