'''
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
Have you met this question in a real interview? Yes
Example
For the following binary search tree, in-order traversal by using iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root =  root.left

    #@return: True if there has next node, or false
    def hasNext(self):
        res = True if self.stack else False
        return res
    #@return: return next node
    def next(self):
        root = self.stack.pop()
        toReturn = root.val
        root = root.right
        while root:
            self.stack.append(root)
            root = root.left
        return toReturn
