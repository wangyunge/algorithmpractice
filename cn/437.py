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
        :rtype: int
        """
        self.res = 0
        def _dfs(node, table, cul):
            if node:
                cul += node.val
                if cul - targetSum in table:
                    self.res += table[cul-targetSum]
                if cul in table:
                    table[cul] += 1
                else:
                    table[cul] = 1
                _dfs(node.left, table, cul)
                _dfs(node.right, table, cul)
                table[cul] -= 1
        _dfs(root, {0:1}, 0) # B arr need a start
        return self.res

