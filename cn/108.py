# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def _buildBST(i, j):
            if i > j:
                return None
            mid = (i+j) // 2
            node = TreeNode(nums[mid])
            node.left = _buildBST(i, mid-1)
            node.right = _buildBST(mid+1, j)
            return node

        i = 0
        j = len(nums) - 1
        return _buildBST(i, j)

