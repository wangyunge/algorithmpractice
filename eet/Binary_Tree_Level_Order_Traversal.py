"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""


from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        laddar = []
        last_level = 0
        if not root:
            return res
        queue = deque()
        queue.append([root, 0])
        while queue:
            root, level = queue.popleft()
            if root.left:
                queue.append([root.left, level + 1])
            if root.right:
                queue.append([root.right, level+ 1])

            if level == last_level:
                laddar.append(root.val)
            else:
                res.append(laddar)
                laddar = [root.val]
            last_level = level
        res.append(laddar)
        return res




