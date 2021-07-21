"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_queue = deque()
        node_queue.append((root, 1))
        res = None
        level = 0
        while node_queue:
            cur_node, cur_level = node_queue.popleft()
            if cur_level != level:
                res = cur_node
                level = cur_level
            if cur_node.left:
                node_queue.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                node_queue.append((cur_node.right, cur_level + 1))
        return res.val 









        