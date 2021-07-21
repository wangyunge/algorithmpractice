'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Have you met this question in a real interview? Yes
Example
Given the below binary tree:

  1
 / \
2   3
return 6.
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
    @return: An integer
    """
    def maxPathSum(self, root):        
        self.res = float('-inf')
        self.DFS(root)
        return self.res
    def DFS(self,root):
        if not root:
            return 0
        leftRes = self.DFS(root.left)
        rightRes = self.DFS(root.right)
        origVal = root.val
        res = max(origVal,leftRes+rightRes+origVal,leftRes+origVal,rightRes+origVal)
        self.res = max(self.res,res)
        return max(origVal,leftRes+origVal,rightRes+origVal)
