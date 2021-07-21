'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Have you met this question in a real interview? Yes
Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        self.res = True
        if root:
            self.DFS(root.left,float('-inf'),root.val)
            self.DFS(root.right,root.val,float('inf'))
        return self.res
    def DFS(self,root,bottom,top):
        if root:
            if root.val <= bottom or root.val >= top:
                self.res = False 
            else:
                self.DFS(root.left,bottom,root.val)
                self.DFS(root.right,root.val,top)
