# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        big = max(p.val, q.val)
        small = min(p.val, q.val)
        def _dfs(node):
            if node:
                if small <= node.val and node.val <= big:
                    return node
                elif node.val < small:
                    return _dfs(node.right)
                else:
                    return _dfs(node.left)
        return _dfs(root)

