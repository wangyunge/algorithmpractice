"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root is not None or len(stack) > 0:
            if root is not None:
                stack.append((root, 0))
                stack.append((root.right, 1)) 
                root = root.left
            else:
                pop_root, flag = stack.pop()
                if flag == 0:
                    res.append(pop_root.val)
                if flag == 1:
                    root = pop_root
        return res                 
