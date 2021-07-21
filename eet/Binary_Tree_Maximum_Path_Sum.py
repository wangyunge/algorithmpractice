'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.Max = float("-inf")
            self.DFS(root)
        else:
            self.Max = 0
        return self.Max
        
    def DFS(self,root):
        if root:
            self.DFS(root.left)
            self.DFS(root.right)
            left_val = root.left.val if root.left else 0
            right_val = root.right.val if root.right else 0
            self.Max = max(self.Max,root.val + left_val + right_val,left_val + root.val,right_val + root.val,root.val)
            root.val  = max(root.val,left_val + root.val,right_val + root.val)

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')

        def _dfs(root):
            if not root:
                return 0
            left_depth = max(0, _dfs(root.left))
            right_depth = max(0, _dfs(root.right))
            self.res = max(self.res, left_depth + right_depth + root.val )

            return max(left_depth, right_depth) + root.val
        _dfs(root)
        return self.res

