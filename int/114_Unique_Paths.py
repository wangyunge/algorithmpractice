'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 Notice

m and n will be at most 100.

Have you met this question in a real interview? Yes
Example
1,1
1,2
1,3
1,4
1,5
1,6
1,7
2,1






3,1





3,7

Above is a 3 x 7 grid. How many possible unique paths are there?
'''
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        den1 = 1
        den2 = 1
        nor = 1
        for i in xrange(1,m+n-1):
            nor *= i 
        for i in xrange(1,m):
            den1 *= i 
        for i in xrange(1,n):
            den2 * = i 
        return nor/(den1*den2)