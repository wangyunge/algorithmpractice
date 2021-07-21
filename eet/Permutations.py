"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from collections import deque
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums = sorted(nums)
        res = []
        def _dfs(pos, path):
            for idx in range(pos+1,len(nums)):
                _dfs()

class Solution(object):
    def permute(self,nums):
        res =[]
        nums.sort()
        pool = nums
        stack=[([],pool)]
        while stack:
            (per,pool) = stack.pop()
            if len(per)==len(nums):
                res.append(per)
            else:
                last=None
                for swap in xrange(0,len(pool)):
                    if last!=pool[swap]:
                        n_pool =tuple(pool)
                        n_pool = list(n_pool)
                        n_pool[swap] = pool[0]
                        stack.append((per+[pool[swap]],n_pool[1:]))
                        last = pool[swap]
        return res

class Solution(object):
    def permute(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        def _backtrack(mid_res):
            if len(mid_res) == len(nums):
                res.append(mid_res)
            else:
                for item in nums:
                    if item not in mid_res:
                        _backtrack(mid_res + [item])
        _backtrack([])
        return res