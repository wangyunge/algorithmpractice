"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        def _dfs_check(left_node, right_node):
            if not left_node and not right_node:
                return True
            elif left_node and right_node:
                if left_node.val == right_node.val:
                    return _dfs_check(left_node.left, right_node.right) and _dfs_check(left_node.right, right_node.left)
                else:
                    return False
            else:
                return False
        return _dfs_check(root.left, root.right)



        if root:
            if root.left and root.right:
                if root.left != root.right:
                    return False 
                else:
                    return isSymmetric(root.left) and isSymmetric(root.right)

            else:
                return root.left == root.right
        return True 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _check_pair(left_node, right_node):
            if not left_node and not right_node:
                return True
            elif left_node and right_node:
                if left_node.val == right_node.val:
                    return True 
                else:
                    return False
            else:
                return False

        if not root:
            return True
        stack = []
        pair = (root.left, root.right)
        while pair[0] or pair[1] or stack:
            if pair[0] or pair[1]:
                if not _check_pair(pair[0], pair[1]):
                    return False 
                stack.append(pair)
                pair = (pair[0].left, pair[1].right)
            else:
                pair = stack.pop()
                pair = (pair[0].right, pair[1].left)
        return True 
