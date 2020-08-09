"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        self.sum = sum
        self._dfs(root, [])
        return self.res
    def _dfs(self, root, path_sums):
        if root:
            path_sums.append(0)
            new_path_sums = []
            for sum_item in path_sums:
                sum_item += root.val
                if sum_item == self.sum:
                    self.res += 1
                new_path_sums.append(sum_item)

            self._dfs(root.left, new_path_sums)
            self._dfs(root.right, new_path_sums)


        
"""
Note : Similar to 560. Subarray Sum Equals K. The difference of two sums with two end and root is the sum between two endpoints.

"""