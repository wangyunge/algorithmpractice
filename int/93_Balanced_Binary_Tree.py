'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Have you met this question in a real interview? Yes
Example
Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.
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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
    	self.res = True
        if not root:
        	return True
        leftH = self.depthDFS(root.left)
        rightH = self.depthDFS(root.right)
        if abs(leftH - rightH) > 1:
        	self.res = False 
        return self.res
    def depthDFS(self,root):
    	if not root:
    		return 1
    	leftH = self.depthDFS(root.left)
        rightH = self.depthDFS(root.right)
        if abs(leftH - rightH) > 1:
        	self.res = False 
        return max(leftH,rightH)+1
