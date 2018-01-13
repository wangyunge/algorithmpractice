'''
Given preorder and inorder traversal of a tree, construct the binary tree.

 Notice

You may assume that duplicates do not exist in the tree.

Have you met this question in a real interview? Yes
Example
Given in-order [1,2,3] and pre-order [2,1,3], return a tree:

  2
 / \
1   3
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
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        for j in xrange(len(inorder)):
            if inorder[j] == preorder[0]:
                break
            self.DFS(preorder[1:],inorder[:j],root,True)
            self.DFS(preorder[1:],inorder[j+1:],root,False)
        return root 
    def DFS(self,preorder,inorder,parent,left):
        found = False
        for i in xrange(0,len(preorder)):
            for j in xrange(0,len(inorder)):
                if inorder[j] == preorder[i]:
                    found = True 
                    break
            if found:
                break
        if found:
            root = TreeNode(inorder[i])
            if left:
                parent.left = root 
            else:
                parent.right = root 
            self.DFS(preorder[i+1:],inorder[:j],root,True)
            self.DFS(preorder[i+1:],inorder[j+1:],root,False)

def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root
