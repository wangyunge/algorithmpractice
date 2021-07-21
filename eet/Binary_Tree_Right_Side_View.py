`'''
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


from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        res = []
        q = deque()
        q.append((root, 1))
        head = None
        last_level = 0
        while q :
            head, level = q.popleft()
            if last_level != level:
                res.append(head.val)
            last_level = level
            if head.right:
                q.append((head.right, level+1))
            if head.left:
                q.append((head.left, level+1))
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

