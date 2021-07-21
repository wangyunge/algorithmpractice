'''
叶子节点为空
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def _dfs_check(a, b):
            if a and b:
                if a.val != b.val:
                    return False
                return _dfs_check(a.left, b.left) and _dfs_check(a.right, b.right)
            elif not a and not b:
                return True
            else:
                return False
        return _dfs_check(p, q)
