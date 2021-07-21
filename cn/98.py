# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        def _dfs(node, lb, rb):
            if node:
                if self.res and node.left:
                    if lb < node.left.val and node.left.val < node.val:
                        _dfs(node.left, lb, node.val)
                    else:
                        self.res = False
                if self.res and node.right:
                    if node.val < node.right.val and node.right.val < rb:
                        _dfs(node.right, node.val, rb)
                    else:
                        self.res= False
        _dfs(root, float('-inf'), float('inf'))
        return self.res
