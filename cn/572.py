# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def _check(source, target):
            if source and target:
                if source.val == target.val:
                    return _check(source.left, target.left) and _check(source.right, target.right)
                else:
                    return False
            elif not source and not target:
                return True
            else:
                return False
        def _dfs(a, b):
            if a:
                if _check(a, b):
                    return True
                return _check(a.left, b) or _check(a.right, b)
        if not t:
            return True
        return _dfs(s, t)
