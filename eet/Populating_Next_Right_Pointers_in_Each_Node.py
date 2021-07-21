"""

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        queue = deque()
        prev = None
        queue.append([0, root])
        last_level = -1
        while queue:
            level, node = queue.popleft()
            if last_level == level:
                prev.next = node
            if node.left:
                queue.append([level+1, node.left]) 
            if node.right:
                queue.append([level+1, node.right])
            last_level = level
            prev = node
        return root




class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def _dfs(root):
            """
            Use the next pointer to achieve a O(1) solution
            """
