'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Subscribe to see which companies asked this question
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
    
    def generateByList(self,list):
        root = TreeNode(list[0])
        for i in xrange(1,len(list)):
            self.BSTappend(root,list[i])
        return root
    def BSTappend(self,root,num):
        parent = root
        while root:
            parent = root
            if root.val < num:
                root = root.right
            else:
                root = root.left
        if parent.val < num:
            parent.right = TreeNode(num)
        else:
            parent.left = TreeNode(num)

            