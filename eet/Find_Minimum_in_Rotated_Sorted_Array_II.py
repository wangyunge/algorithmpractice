'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R = len(nums)-1
        mid = L + (R-L)/2
        while L < R:
            mid = L + (R-L)/2
            if mid == L:
                break
            if nums[mid] < nums[R]:
                R = mid
            elif nums[mid] > nums[R]:
                L = mid 
            else:
                R-=R
        res = min(nums[mid],nums[mid+1]) if mid+1 < len(nums) else nums[mid]
        return res
    def findMin(self,nums):
        res = float("inf")
        for n in nums:
            res = min(res,n)
        return res