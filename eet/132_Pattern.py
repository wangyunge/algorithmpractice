"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for a in range(len(nums)):
            j = float('-inf') 
            for b in range(a, len(nums)):
                if nums[b] > nums[a] and nums[b] < j:
                    return True
                j = max(j, nums[b])
        return False


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        interval = []
        cur_min = nums[0]
        cur_max = nums[0]
        for a in range(1, len(nums)):
            if nums[a] > cur_min and nums[a] < cur_max:
                return True
            elif nums[a] < cur_min:
                interval.append((cur_min, cur_max))
                cur_max = nums[a]
                cur_min  = nums[a]
            elif nums[a] > cur_max:    
                while interval and  interval[-1][0] < nums[a]:
                    last_min, las_max = interval.pop()
                    if last_min < nums[a] and las_max > nums[a]:
                        return True 
                cur_max = nums[a]
        return False





        