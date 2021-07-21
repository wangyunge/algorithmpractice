# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        def _dfs_ser(node):
            if node:
                res.append(str(node.val))
                _dfs_ser(node.left)
                _dfs_ser(node.right)
            else:
                res.append('#')
        _dfs_ser(root)
        return ''.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def _dfs_des(i):
            if data[i] == '#':
                return None, i+1
            else:
                node = TreeNode(int(data[i]))
                node.left, i = _dfs(i+1)
                node.right, i = _dfs(i+1)
                return node, i
        root, _ = _dfs_des(0)
        return root





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
