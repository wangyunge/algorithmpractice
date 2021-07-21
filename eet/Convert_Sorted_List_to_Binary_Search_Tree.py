'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sortedArray = []
        while head:
            sortedArray.append(head.val)
            head = head.next
        root = self.buildBST(sortedArray)
        return root
    def buildBST(self,sortedArray):
        if not sortedArray:
            return None
        mid = len(sortedArray)/2
        root = TreeNode(sortedArray[mid])
        root.left = self.buildBST(sortedArray[:mid])
        root.right = self.buildBST(sortedArray[mid+1:])
        return root
