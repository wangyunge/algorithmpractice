"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q
        res, _, _ = self._dfs(root)
        return res

    def _dfs(self, root):
        if not root:
            return None, False, False

        left_res, left_p, left_q = self._dfs(root.left)
        right_res, right_p, right_q = self._dfs(root.right)

        cur_p = True if root.val == p.val else False 
        cur_q = True if root.val == q.val else False 

        if left_res is not None:
            return left_res, True, True 
        if right_res is not None:
            return right_res, True, True

        find_p = False
        if cur_p or left_p or right_p:
            find_p = True 
        find_q = False
        if cur_q or left_q or right_q:
            find_q = True  

        if find_p and find_q:
            return root, True, True

        return None, find_p, find_q

"""
Note:
Recurring can pass message back by using return. So we don't need to do the dfs twice(Check and Search)
"""