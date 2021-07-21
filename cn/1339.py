"""
binary,
1 edge
2 subtree
subtree sum ?
mod 7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        M = 1000000007
        def _mod(num):
            k = num // M
            mod = num % M
            return (k, mod)
        def _mod_multiply(a, b):
            k = a[0]*b[0]*M + (a[0]*b[1]+a[1]*b[0]) +
            mode =
        def _dfs(node):
            if node:
                l = _dfs(node.left)
                r = _dfs(node.right)
                self.res = max(self.res, l*(r+node.val), r*(l+node.val))
                return l+r+node.val
            return 0
        _dfs(root)
        return int(self.res)



