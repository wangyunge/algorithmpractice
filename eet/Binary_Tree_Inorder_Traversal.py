'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

Subscribe to see which companies asked this question
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.res = []
        if root.left:
            self.Travel(root.left)
        self.res.append(root.val)
        if root.right:
            self.Travel(root.right)
        return self.res
        
    def Travel(self,root):
        if root.left :
            self.Travel(root.left)
        self.res.append(root.val)
        if root.right:
            self.Travel(root.right)

    def inorderTraversal(self, root):
        if not root:
            return []
        stack =[]
        table = {}
        res = []
        Begain = True
        while Begain or stack:
            Begain = False
            if root not in table:
                table[root] = 1
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                if root.left:
                    stack.append(root.left)
            else:
                res.append(root.val)
            root = stack.pop()
        return res

    def inorderTraversal(self, root):
        res = []
        stack = []
        while root is not None or len(stack) > 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res 