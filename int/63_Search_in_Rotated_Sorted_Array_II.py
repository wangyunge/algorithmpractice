'''
Follow up for Search in Rotated Sorted Array:

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Have you met this question in a real interview? Yes
Example
Given [1, 1, 0, 1, 1, 1] and target = 0, return true.
Given [1, 1, 1, 1, 1, 1] and target = 0, return false.
'''
class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        if not A:
            return False
        left = 0
        right = len(A)-1
        while left < right -1:
            mid = (left+right)/2
            if A[mid] == target:
                return True
            while left < mid and A[left] == A[mid]:
                left += 1
            if A[left] <= A[mid]:
                if A[left] <= target and target <= A[mid]:
                    right = mid
                else:
                    left = mid
            elif A[mid] <= A[right]:
                if A[mid] <= target and target <= A[right]:
                    left = mid
                else:
                    right = mid
        if A[left] == target or A[right] == target:
            return True 
        else:
            return False