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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.left = None
        self.right = None
        self.prev = None
        def _inorder_traverse(node):
            if node:
                _inorder_traverse(node.left)
                if self.prev and self.prev.val > node.val:
                    if not self.left:
                        self.left = self.prev
                    else:
                        self.right = node
                _inorder_traverse(node.right)
        _inorder_traverse(root)
        self.left.val, self.right.val = self.right.val, self.left.val


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.left = None
        self.right = None
        def _search_left(node):
            if node:
                _search_left(node.left)
                if self.left and self.left.val > node.val:
                    return self.left
                self.left = node
                _search_left(node.right)

        def _search_right(node):
            if node:
                _search_right(node.right)
                if self.right and self.right.val < node.val:
                    return self.right
                self.right = node
                _search_right(node.right)
        _search_left(root)
        _search_right(root)
        self.left.val, self.right.val = self.right.val, self.left.val


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
