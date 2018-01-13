'''
Given an unsorted integer array, find the first missing positive integer.

Have you met this question in a real interview? Yes
Example
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        table = set()
        top = 0
        for i in A:
            if i > 0:
                table.add(i)
                top = max(top,i)
        for j in xrange(1,top):
            if j not in table:
                return j
        return top+1