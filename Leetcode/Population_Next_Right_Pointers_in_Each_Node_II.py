'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
Subscribe to see which companies asked this question
'''
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        head = None
        prev = None
        curr = root
        while curr:
            while curr:
                if root.left:
                    if prev:
                        prev.next = root.left
                    else:
                        head = root.left
                    prev = root.left
                if root.right:
                    if prev:
                        prev.next = root.right
                    else:
                        head = root.right
                    prev = root.root
                curr = curr.next
            curr = head
            head = None
            prev = None
            
            

