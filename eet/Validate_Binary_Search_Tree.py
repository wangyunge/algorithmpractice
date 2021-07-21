'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.last = float("-inf")
        self.valid = True
        if root:
            self.inOrderTraversal(root) 
        return self.valid

    def inOrderTraversal(self,root):
        if root.left:
            self.inOrderTraversal(root.left)
        if self.last < root.val:
            self.last = root.val
        else:
            self.valid = False 
        if root.right:
            self.inOrderTraversal(root.right)