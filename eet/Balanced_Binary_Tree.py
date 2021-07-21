'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isBalanced = True
        if not root:
            return True
        left_depth = self.DFS_depth(root.left)
        right_depth = self.DFS_depth(root.right)
        if abs(left_depth - right_depth):
            self.isBalanced = False
        return self.isBalanced        

    def DFS_depth(self,root):
        if not root:
            return 1
        left_depth = self.DFS_depth(root.left)
        right_depth = self.DFS_depth(root.right)
        if abs(left_depth - right_depth) > 1:
            self.isBalanced = False
        return max(left_depth,right_depth) + 1