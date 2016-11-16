'''
Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.

Have you met this question in a real interview? Yes
Example
    1             1
   / \           / \
  2   2   and   2   2
 /             /
4             4
are identical.

    1             1
   / \           / \
  2   3   and   2   3
 /               \
4                 4
are not identical.
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        self.res = True
        self.DFS(a,b) 
        return self.res
    def DFS(self,a,b):
        if a and b:
            if a.val != b.val:
                self.res = False 
            self.DFS(a.left,b.left)
            self.DFS(a.right,b.right)
        elif a or b:
            self.res = False
