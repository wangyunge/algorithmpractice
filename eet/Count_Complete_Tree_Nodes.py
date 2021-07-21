''' Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cnt = 0
        if root:
            self.DFS(root)
        return self.cnt

    def DFS(self,root):
        self.cnt += 1
        if root.left:
            self.DFS(root.left)
        if root.right:
            self.DFS(root.right)



class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt = 0
        def _get_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        def _count_nodes(node):
            left_depth = _get_depth(node.left)
            right_depth = _get_depth(node.right)

            if left_depth == right_depth:
                # left subtree is complete
                cnt = cnt + pow(2, left_depth) -1 + 1 + _count_node(node.right)
            else:
                # right subtree is complete
                cnt = cnt + pow(2, right_depth) -1 + 1 + _count_node(node.left)





