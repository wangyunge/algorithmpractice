'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []   
        queue = Queue.Queue()
        pack = []
        res = []
        flag = True
        queue.put((root,flag))
        while not queue.empty():
            node,level = queue.get()
            if node:
                if flag != level:
                    res.append(pack)
                    flag = level
                    pack =[]
                pack.append(node.val)
                queue.put((node.left,not flag))
                queue.put((node.right,not flag))

        res.append(pack)
        res.reverse()
        return res
