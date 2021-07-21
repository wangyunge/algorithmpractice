"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def _dfs(node, inherent):
            if node:
                honor = inherent.pop()
                saving = node.val % 2 == 0
                left_value = _dfs(node.left, [saving, inherent[0]])
                right_value = _dfs(node.right, [saving, inherent[0]])

                if honor:
                    return left_value + right_value + node.val
                else:
                    return left_value + right_value 
            else:
                return 0
        res = _dfs(root, [False, False])
        return res


