'''
Given a binary tree, return the postorder traversal of its nodes' values.

Have you met this question in a real interview? Yes
Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
 

return [3,2,1].
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        self.res = []
        self.DFS(root)
        return self.res
    def DFS(self,root):
        if root:
            self.DFS(root.left)
            self.DFS(root.right)
            self.res.append(root.val)