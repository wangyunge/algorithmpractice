# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        level = 0
        queue = deque()
        queue.append((root, level+1))
        last_level = level
        res = []
        prev = None
        while queue:
            node, level = queue.popleft()
            if level != last_level:
                if prev is not None :
                    res.append(prev)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            last_level = level
            prev= node.val
        if prev:
            res.append(prev)
        return res


