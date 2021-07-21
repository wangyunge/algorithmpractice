# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def _dfs(node):
            if node:
                if not node.left:
                    return _dfs(node.right) + 1
                if not node.right:
                    return _dfs(node.left) + 1
                return min(_dfs(node.left), _dfs(node.right)) + 1
            else:
                return 0
        return _dfs(root)