# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isBalanced(root):
            if root:
                left_depth, left_balance = _isBalanced(root.left)
                right_depth, right_balance = _isBalanced(root.right)
                bal_res =  left_balance and right_balance and abs(left_depth-right_depth) <= 1
                depth = max(left_depth, right_depth)
                return depth+1, bal_res
            else:
                return 0, True
        _, res = _isBalanced(root)
        return res

"""
check the depth of none
"""
