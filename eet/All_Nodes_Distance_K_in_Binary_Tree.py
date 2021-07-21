"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        res = []
        def _dfs(node, up_dist):
            if node:
                if up_dist + 1 == k:
                    res.append(node.val)

                if node.val == target:
                    up_dist = 0

                left_dist = _dfs(node.left, up_dist+1)
                right_dist = _dfs(node.right, up_idst+1)

                down_dist = min(left_dist, right_dist) + 1
                if down_dist == k:
                    res.append(node.val)
                return down_dist
            else:
                float('inf')



class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        res = []
        def _dfs_left(node, up_dist):
            if node:
                if up_dist + 1 == k:
                    res.append(node.val)

                if node.val == target:
                    up_dist = 0

                left_dist = _dfs(node.left, up_dist+1)
                right_dist = _dfs(node.right, up_idst+1)

                down_dist = min(left_dist, right_dist) + 1
                if down_dist == k:
                    res.append(node.val)
                return down_dist
            else:
                return float('inf')
        def _dfs_right(node, up_dist):
            if node:
                if up_dist + 1 == k:
                    res.append(node.val)

                if node.val == target:
                    up_dist = 0

                right_dist = _dfs(node.right, up_idst+1)
                left_dist = _dfs(node.left, up_dist+1)

                down_dist = min(left_dist, right_dist) + 1
                if down_dist == k:
                    res.append(node.val)
                return down_dist
            else:
                return float('inf')
"""
Notes: Node on path to target and nods
"""
