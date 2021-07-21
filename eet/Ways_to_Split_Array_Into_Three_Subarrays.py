"""
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.


Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 104
"""

class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0
        def _dfs(s1, s2, s3, idx, part):
            if idx == len(nums):
                if part === 2 and s3
            if part == 0:
                _dfs(s1 + nums[idx], s2, s3, idx+1, 0)
                if idx > 0:
                    _dfs(s1 + nums[idx], s2, s3, idx+1, 1)
            elif part == 1:
                if s1 <= nums[idx] + s2:
                    _dfs(s1, s2+nums[idx], s3, idx+1 , 2)
                _dfs(s1, s2+nums[idx], s3, idx+1, 1)
            elif part == 2:
                _dfs(s1, s2, s3 + sum(nums[idx:]), len(nums) -1, 2)


class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx in range(1, len(nums)):
            nums[idx] = nums[idx-1] + nums[idx]
        res = 0
        for i in range(0, len(nums)-2):
            if nums[i] > nums[-1] - nums[i]:
                break
            for j in range(i+1, len(nums)-1):
                if nums[i] <= nums[j] - nums[i] <= nums[-1] - nums[j]:
                    res +=1
        return res




# algo
# Compute prefix array of nums. Any at index i, you want to find index j such at
# prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
# The rest comes out naturally.

# Yunge: It is not that natural. The idea is find the overlap of two feasible range.
# The the key to find the feasible range is to find the split position.

# Implementation

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = 0
        for i in range(1, len(nums)): 
            j = bisect_left(prefix, 2*prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1])//2)
            ans += max(0, min(len(nums), k) - max(i+1, j))
        return ans % 1_000_000_007
# Analysis
# Time complexity O(NlogN)
# Space complexity O(N)

# Edit
# Adding two pointers approach O(N) time

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = j = k = 0 
        for i in range(1, len(nums)): 
            j = max(j, i+1)
            while j < len(nums) and 2*prefix[i] > prefix[j]: j += 1
            k = max(k, j)
            while k < len(nums) and 2*prefix[k] <= prefix[i] + prefix[-1]: k += 1
            ans += k - j 
        return ans % 1_000_000_007