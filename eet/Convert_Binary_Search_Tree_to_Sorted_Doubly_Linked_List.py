"""
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:





We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.





Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def cvtBSTTolinkedList(self, root):
        """
        input: root of a BSt
        ouput: head of doubly linked-list
        """
        dummy = TreeNode()
        self.prev = dummy

        # in-order traversal
        def _dfs(node, prev):
            if node:
                prev = _dfs(node.left, prev)
                prev.right = node
                node.left = prev
                prev = node
                prev = _dfs(node.right, prev)
                return prev
            else:
                return prev
        _dfs(root, dummy)
        return dummy.right

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def cvtBSTTolinkedList(self, root):
        """
        input: root of a BSt
        ouput: head of doubly linked-list
        """
        dummy = TreeNode()
        prev = dummy

        def _dfs(root):
            if root:
                _dfs(root.left)
                prev.right = root
                root.left = prev
                root = prev
                _dfs(root.right)

        _dfs(root)

        return dummy.right
