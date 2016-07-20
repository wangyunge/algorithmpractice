'''
Given preorder and inorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root_val = preorder[0]
        for idx,val in enumerate(inorder):
            if val == root_val:
                left_inorder = inorder[:idx]
                right_inorder = inorder[idx+1:]
                break
        left_preorder = preorder
        right_preorder = [] 
        for idx,val in enumerate(preorder):
            if val in right_inorder:
                left_preorder = preorder[1:idx]
                right_preorder = preorder[idx:]
                break
        
        
        root = TreeNode(root_val)
        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)
        return root
# def buildTree(self, preorder, inorder):
#     if inorder:
#         ind = inorder.index(preorder.pop(0))
#         root = TreeNode(inorder[ind])
#         root.left = self.buildTree(preorder, inorder[0:ind])
#         root.right = self.buildTree(preorder, inorder[ind+1:])
#         return root