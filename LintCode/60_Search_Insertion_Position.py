'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Have you met this question in a real interview? Yes
Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0

'''
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if not A:
            return 0
        left = 0
        right = len(A)-1
        while left < right-1:
            mid = (left+right)/2
            if A[mid] > target:
                right = mid
            elif A[mid] < target:
                left = mid
            else:
                return mid
        if A[left] >= target:
            return left
        elif A[right]< target:
            return right+1
        else:
            return right