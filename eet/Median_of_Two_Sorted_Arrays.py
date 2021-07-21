"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        k = (len(nums1) + len(nums2)) // 2
        odds = (len(nums1) + len(nums2)) % 2

        left = 0 
        right = (len(nums1) + len(nums2)) // 2 - 1
        while left <= right:
            mid = (left + right) // 2
            cur = L - mid
            if cur >= 0:
                if nums1[mid] == nums2[cur]:
                    return  nums1[mid]
                if nums1[mid] < nums2[cur]:
                    left = mid + 1
                else:
                    right = mid -1 
            else:

        return nums1[mid]
             
