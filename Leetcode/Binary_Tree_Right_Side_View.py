'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.bfsList = []
        self.BFS(root)
        for stack in self.bfsList:
            res.append(stack[0])
        return res
    def BFS(self,root):
        stack = []
        queue = Queue.Queue()
        queue.put((root,True))
        level = True
        while not queue.empty():
            node,flag = queue.get()
            if flag != level:
                self.bfsList.append(stack)
                level = flag
                stack = []
            stack.append(node.val)
            if node.right:
                queue.put(node.right,not flag)
            if node.left:
                queue.put(node.left,not flag)
        if stack:
            self.bfsList.append(stack)

