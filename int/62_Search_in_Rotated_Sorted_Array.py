'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Have you met this question in a real interview? Yes
Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.
'''
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if not A:
            return -1
        left = 0
        right = len(A)-1
        while left < right :
            mid = (left+right)/2
            if target == A[mid]:
                return mid
            if target > A[mid]:
                if target <= A[right]:
                    left = mid + 1
                else:
                    right = mid -1
            if target < A[mid]:
                if target >= A[left]:
                    right = mid -1
                else:
                    left = mid + 1
        if A[left] == target:
            return left
        else:
            return -1
def main():

    sol = Solution()
    sol.search([0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1], -9)
if __name__ == '__main__':
    main()