"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def _is_duplicate(r1, r2):
            if r1 and r2:
                if r1.val = r2.val:
                    du_left = _is_duplicate(r1.left, r2.left)
                    du_right = _is_duplicate(r1.right, r2.right) 
                    return du_left and du_right
                else:
                    False
            elif not r1 and not r2:
                return True
            else:
                return False

        table = {} # for same value , {value:[node1, node2...]}

        # File the table

        # check every pair in same key 

       
"""
Note:
Approach 1: convert tree to string , then hash to find duplicate 
"""


    def findDuplicateSubtrees(self, root):
        self.type_id_gen = 0
        duplicated_subtrees = []
        type_to_freq = defaultdict(int)
        type_to_id = {}
        
        def dfs(node):
            if not node:
                return -1
            type_id_left, type_id_right = (dfs(ch) for ch in (node.left, node.right))
            tree_type = (node.val, type_id_left, type_id_right)
            freq = type_to_freq[tree_type]
            if freq == 0:
                type_id = self.type_id_gen
                self.type_id_gen += 1
                type_to_id[tree_type] = type_id
            elif freq == 1:
                type_id = type_to_id[tree_type]
                duplicated_subtrees.append(node)
            else:
                type_id = type_to_id[tree_type] 
            type_to_freq[tree_type] += 1
            return type_id
            
        dfs(root)
        return duplicated_subtrees  


