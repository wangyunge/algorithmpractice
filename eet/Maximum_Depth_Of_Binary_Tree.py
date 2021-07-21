'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Subscribe to see which companies asked this question
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        level = 0
        self.DFS(root,level)
        return self.res
    def DFS(self,root,level):
        if root:
            level+=1
            self.res = max(level,self.res)
            self.DFS(root.left,level)
            self.DFS(root.right,level)