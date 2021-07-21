'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Have you met this question in a real interview? Yes
Example
Given a binary tree as follow:

  1
 / \ 
2   3
   / \
  4   5
The minimum depth is 2.
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
    def minDepth(self, root):
        if not root:
            return 0
        self.res = float('inf')
        self.DFS(root,0)
        return self.res 
    def DFS(self,root,depth):
        if root:
            if not root.left and not root.right:
                self.res = min(self.res,depth+1)
            self.DFS(root.left,depth+1)
            self.DFS(root.right,depth+1)
