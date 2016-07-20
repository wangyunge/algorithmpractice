'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_val = postorder.pop()
            idx = inorder.index(root_val)
            root = TreeNode(root_val)
            root.right = self.buildTree(inorder[idx+1:],postorder)
            root.left = self.buildTree(inorder[:idx],postorder)
            return root
        else:
            return None