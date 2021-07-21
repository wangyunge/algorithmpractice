class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def _dfs(i, path):
            if i == len(nums):
                res.append(path)
            else:
                _dfs(i+1, path + [nums[i]])
                _dfs(i+1, path)
        _dfs(0, [])
        return res


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
