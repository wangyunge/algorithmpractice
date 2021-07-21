# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.res = []
        def _dfs(node, path, s):
            if node:
                s += node.val
                if not node.left and not node.right:
                    if  s == targetSum:
                        self.res.append(path+ [node.val])
                _dfs(node.left, path + [node.val], s)
                _dfs(node.right, path + [node.val], s)
        _dfs(root, [], 0)
        return self.res
