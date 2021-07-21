'''
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Have you met this question in a real interview? Yes
Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
'''
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        left = 0
        right = len(A)-1
        while left < right:
            if A[left] != elem:
                left += 1
            elif A[right] == elem:
                right -= 1
            else:
                A[left],A[right] = A[right],A[left]
        A = A[:left]
        return left
    def removeElement(self, A, elem):
        begin = 0
        for i in xrange(len(A)):
            if A[i] != elem:
                A[begin],A[i] = A[i],A[begin]
                begin += 1
        return begin

