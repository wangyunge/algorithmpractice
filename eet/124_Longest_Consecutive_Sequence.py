'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Have you met this question in a real interview? Yes
Clarification
Your algorithm should run in O(n) complexity.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
'''
class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, nums):
        nums = set(nums)
        maxLen = 0
        while nums:
            first = last = nums.pop()
            while first-1 in nums:
                first -= 1
                nums.remove(first)
            while last+1 in nums:
                last += 1
                nums.remove(last)
            maxLen = max(maxLen,last-first+1)
        return maxLen