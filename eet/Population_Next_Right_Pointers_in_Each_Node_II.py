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
        cur = root
        while cur:
            level_head = cur.left if cur.left else cur.right
            while cur:
                if cur.left:
                    if cur.right:
                        cur.left.next = cur.right
                    elif cur.next:
                        if cur.next.left:
                            cur.left.next = cur.next.left
                        else:
                            cur.left = cur.next.right
                    else:
                        cur.left.next = cur.next
                if cur.right:
                    if cur.next:
                        if cur.next.left:
                            cur.right.next = cur.next.left
                        else:
                            cur.right.next = cur.next.right
                    else:
                        cur.right.next = cur.next
                cur = cur.next
            cur = level_head
        return root



class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        head = None
        prev = None
        cur = root
        while cur:
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur = head
            head = None
            prev = None
        return root

[1,2,3,4,null,null,5]
Output
[1,#,2,#,4,#]
Diff
Expected
[1,#,2,3,#,4,5,#]

