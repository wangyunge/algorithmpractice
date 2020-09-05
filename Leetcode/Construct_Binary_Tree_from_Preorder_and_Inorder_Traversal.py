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

        root = _buildTree(0, 0, len(inorder)) 


        def _buildTree(pre_left, in_left, in_right):

            for pre_idx in raneg(pre_left, len(preorder)):   # Building the tree in preorder can gauarntee the first element in preorder is root
                for in_idx in range(in_left, in_right):
                    if preorder[pre_idx] == inorder[in_idx] :
                        root = TreeNode(preorder[pre_idx])
                        root.left = _buildTree(pre_idx+1, in_left, in_idx)
                        root.right = _buildTree(pre_idx+1, in_idx+1, in_right)
                        break
            return root

"""
Approach #1 
Recursion can make every head in preorder is head
""" 
def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root

"""
Approach #2
The position of right child in preordr can be calculated by length of left children in inorder
""" 
