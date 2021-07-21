
"""
1. left + right + node.val
2. left + node.val
3. right + node.val
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        def _dfs(node):
            if node:
                lv = max(0, _dfs(node.left))
                rv = max(0, _dfs(node.right))
                self.res = max(self.res, lv + node.val + rv)
                return node.val + max(lv, rv)
            else:
                return 0
        _dfs(root)
        return self.res

