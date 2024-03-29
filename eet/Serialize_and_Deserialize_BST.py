"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""





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
        def _dfs(root):
            if root:
                res.append(str(root.val))
                _dfs(root.left)
                _dfs(root.right)
        _dfs(root)
                
        return ''.join(res)



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def _build(k, parent):
            if k >= len(data):
                return None, k

            root = TreeNode(int(data[k]))
            val = int(data[k+1])
            parent = parent if parent else float('-inf')
            if parent <= val and val <= root.val:
                root.left, k = _build(k+1, root.val)
            val = int(data[k+1])
            parent = parent if parent else float('inf')
            if root.val <= val and val <= parent:
                root.right, k= _build(k+1, root.val)

            return root, k
        return _build(0, None)
            


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))