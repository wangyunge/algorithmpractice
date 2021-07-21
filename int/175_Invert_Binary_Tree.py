'''
Invert a binary tree.

Have you met this question in a real interview? Yes
Example
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        if root:
            root.left,root.right = root.right,root.left
            self.invertBinaryTree(root.left)
            self.invertBinaryTree(root.right)
