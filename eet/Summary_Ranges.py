"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return res 
        left = right = 0
        while right <= len(nums) and left < len(nums):
            if right < len(nums) and nums[right] - nums[left] == right - left:
                right += 1
            else:
                if left == right-1:
                    res.append(str(nums[left]))
                else:
                    temp = str(nums[left]) + "->" + str(nums[right-1])
                    res.append(temp)

                left = right
        return res 