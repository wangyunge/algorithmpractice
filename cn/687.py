"""

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def _dfs(node):
            if not node:
                return None, 0
            if node:
                lv, ll = _dfs(node.left)
                rv, rl = _dfs(node.right)
                if node.val == lv and node.val == rv:
                    self.res = max(self.res, ll + rl + 1)
                    return node.val, max(ll, rl) + 1
                elif node.val == lv:
                    self.res = max(self.res, ll+1)
                    return node.val, ll+1
                elif node.val == rv:
                    self.res = max(self.res, rl+1)
                    return node.val, rl+1
                else:
                    return node.val, 1
        _dfs(root)
        return max(self.res-1, 0)





