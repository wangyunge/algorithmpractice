'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.sum = sum
        self.DFS(root,[])
        return self.res
    def DFS(self,root,path):
        if root:
            val = root.val
            if root.left or root.right:
                self.DFS(root.left,path + [val])
                self.DFS(root.right,path + [val])
            elif sum(path)+val == self.sum:
                self.res.append(path+[val])