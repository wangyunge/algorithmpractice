'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Notice

You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Have you met this question in a real interview? Yes
Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
'''
class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        if not B:
            return 
        mainIndex = 0
        secIndex = m
        comIndex = 0
        while mainIndex < m+n:
            if not A[mainIndex]:
                A[mainIndex] = B[comIndex]
                comIndex += 1
            elif A[mainIndex] > B[comIndex]:
                A[mainIndex],B[comIndex] = B[comIndex],A[mainIndex]
                for i in xrange(comIndex,n-1):
                    if B[i] > B[i+1]:
                        B[i],B[i+1] = B[i+1],B[i]
                    else:
                        break
            mainIndex += 1
    def mergeSortedArray(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1