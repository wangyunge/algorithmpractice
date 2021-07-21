# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.n1 = None
        self.n2 = None
        self.prev = ListNode(float('-inf'))
        def _dfs(node):
            if node:
                _dfs(node.left)
                if self.prev.val > node.val:
                    if not self.n1:
                        self.n1 = self.prev 
                    self.n2 = self.node
                self.prev = node
                _dfs(node.right)
        _dfs(root)
        if self.n1 and self.n2:
            self.n1.val, self.n2.val = self.n2.val, self.n1.val



