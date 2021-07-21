'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.parent = None
        self.DFS(root)
    def DFS(self,root):
        if root:
            left = root.left
            right = root.right
            if self.parent:
                self.parent.right = root
                self.parent.left = None
            self.parent = root
            self.DFS(left)
            self.DFS(right)