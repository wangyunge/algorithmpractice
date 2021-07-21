# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def _find(node, parent, on_left):
            if node:
                if node.val == key:
                    if node.left and node.right:
                        _move(node.left, node.right)
                        if on_left:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                    elif node.left:
                        if no_left:
                            parent.left = node.left
                        else:
                            parent.right = node.right
                    else:
                        if on_left:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                else:
                    _find(node.left, node, True)
                    _find(node.right, node, False)


        def _move(need, cur):
            if cur.left:
                _move(need, cur.left)
            else:
                cur.left = need
        dummy = TreeNode()
        dummy.left = root
        _find(dummy.left, dummy, True)
        return dummy.left


