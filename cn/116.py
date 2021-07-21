"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def _dfs(node):
            if node:
                if node.left and node.right:
                    node.left.next = node.right
                    node.right.next = node.next.left if node.next else None
                    _dfs(node.left)
                    _dfs(node.right)
        _dfs(root)
        return root



