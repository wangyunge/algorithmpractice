'''
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Have you met this question in a real interview? Yes
Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A:
            return [-1,-1]
        if len(A)==1 and A[0]==target:
            return [0,0]
        left = 0
        right = len(A)-1
        searched = False
        while left < right-1:
            mid = (left+right)/2
            if A[mid] < target:
                left = mid
            elif A[mid] > target:
                right = mid
            else:
                searched = True
        if A[left] == target or A[right] == target:
            searched = True
            mid = left if A[left] == target else right
        if searched:
            rb = lb = mid
            while left < lb-1:
                lm = (left+lb)/2
                if A[lm] < target:
                    left =mid
                else:
                    lb = mid
                lb = lb if A[left]<target else left
            while rb < right-1:
                rm = (right+rb)/2
                if A[rm] == target:
                    rb = mid
                else:
                    right = mid
                rb = rb if A[right]> target else right
            return [lb,rb]
        else:
            return [-1,-1]

    def searchRange(self, nums, target):
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1] 