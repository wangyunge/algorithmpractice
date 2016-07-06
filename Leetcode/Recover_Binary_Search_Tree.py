'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
Subscribe to see which companies asked this question

Show Tags
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.last = float("-inf")
        self.swapped = []
        if root:
            self.inOrderTraversal(root)
            self.swapped[0].val,self.swapped[1] = self.swapped[1],self.swapped[0]
    def inOrderTraversal(self,root):
        if root.left:
            self.inOrderTraversal(root.left)
        if self.last > root.val:
            self.swapped.append(root)
        else:
            self.last = root.val
        if root.right:
            self.inOrderTraversal(root.right)