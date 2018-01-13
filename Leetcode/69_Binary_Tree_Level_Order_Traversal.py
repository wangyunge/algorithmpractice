'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Have you met this question in a real interview? Yes
Example
Given binary tree {3,9,20,#,#,15,7},

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
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        from Queue import Queue
        queue = Queue()
        res = []
        pack = []
        queue.put((root,True))
        thisLevel = True
        while not queue.empty():
            (node,level) = queue.get()
            if thisLevel != level:
                res.append(pack)
                pack = []
                thisLevel = level
            if node:
                pack.append(node.val)
                queue.put((node.left,not level))
                queue.put((node.right,not level))
        return res
