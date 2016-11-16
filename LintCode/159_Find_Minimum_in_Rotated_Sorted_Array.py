'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

You may assume no duplicate exists in the array.

Have you met this question in a real interview? Yes
Example
Given [4, 5, 6, 7, 0, 1, 2] return 0
'''
class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if not nums:
            return 0
        left = 0
        right = len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]
        mid = (left+right)/2
        while left < right-1:
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right =  mid
        return min(nums[left],nums[right])