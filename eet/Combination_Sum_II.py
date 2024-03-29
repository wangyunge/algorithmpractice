"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Duplicate in candidates

        res = []
        def _dfs(idx, path, sum_up):
            for cur in range(idx+1, len(candidates)):
                new_sum = sum_up + candidates[cur]
                if new_sum == target:
                    res.append(path + [candidates[cur]])
                elif new_sum < target:
                    _dfs(cur, path + [candidates[cur]], new_sum)
        _dfs(0, [], 0)
        return res

