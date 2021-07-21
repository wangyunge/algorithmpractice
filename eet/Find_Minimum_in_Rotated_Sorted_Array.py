'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R = len(nums) - 1
        mid = (L+R)/2
        while L < R:
            mid = (L+R)/2
            if L==mid:
                break
            if nums[mid] > nums[R]:
                L = mid
            else:
                R = mid
        if mid+1 <= len(nums)-1:
            res = min(nums[mid],nums[mid+1])
        else:
            res = nums[mid]
        return res