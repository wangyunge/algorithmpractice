'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
Subscribe to see which companies asked this question
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = Queue.Queue()
        res = []
        pack = []
        change_level = True
        queue.put((root,change_level))
        while not queue.empty():
            (node,level) = queue.get()
            if node:
                if change_level != level:
                    if level:
                        pack.reverse()
                    res.append(pack)
                    pack = []
                    change_level = not change_level
                pack.append(node.val)

                queue.put((node.left,not change_level))
                queue.put((node.right,not change_level))
        if level:
            pack.reverse
        res.append(pack)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import Queue
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = []
        stack.append(root)
        res = []
        cur = 0
        while stack:
            if stack[-1][1] == cur:
                node, flag = stack.pop()
                if cur == 0:
                    if node.left:
                        stack.append((node.left, ))


        