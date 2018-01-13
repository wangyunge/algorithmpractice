'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        pos = 1
        for i in xrange(2,len(A)):
            if A[i] != A[pos-1]:
                pos += 1
                A[pos] = A[i]
        return pos+1    