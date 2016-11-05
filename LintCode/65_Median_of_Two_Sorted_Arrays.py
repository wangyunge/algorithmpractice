'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Have you met this question in a real interview? Yes
Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.
'''
class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        LA = len(A)
        LB = len(B)
        even = True if (LA+LB)%2==0 else False
        indexA = 0
        indexB = 0
        counter = 0
        mid = (LA+LB)/2
        while counter <= mid:
            if indexA >= LA:
                curr = B[indexB]
                indexB +=1
            elif indexB >= LB:
                curr = A[indexA]
                indexA +=1
            else:
                if A[indexA] < B[indexB]:
                    curr = A[indexA]
                    indexA += 1
                else:
                    curr = B[indexB]
                    indexB += 1
            if counter == mid-1:
                prev = curr
            counter += 1
        if even:
            return 1.0*(prev+curr)/2
        else:
            return curr