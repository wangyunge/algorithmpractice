"""
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Constraints:

The given binary tree will have between 1 and 3000 nodes.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque()
        queue.append((1, root, 0))
        last_level = 0
        res = 0
        level_min = float('inf')
        level_max = float('-inf')
        while queue:
            level, cur , idx = queue.popleft()
            if last_level != level:
                res = max(res, level_max-level_min)
                level_min = float('inf')
                level_max = float('-inf')
            last_lavel = level
            level_min = min(level_min, idx)
            level_max = max(level_max, idx)
            if cur.left:
                queue.append((level+1, cur.left, 2*idx+1))
            if cur.right:
                queue.append((level+1, cur.right, 2*idx+2))
        res = max(res, level_max-level_min)
        return res + 1





