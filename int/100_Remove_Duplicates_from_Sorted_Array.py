'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Have you met this question in a real interview? Yes
Example
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        if not A:
            return 0
        pos = 0
        for i in xrange(1,len(A)):
            if A[i] != A[i-1]:
                pos += 1
                A[pos] = A[i]
        return pos+1