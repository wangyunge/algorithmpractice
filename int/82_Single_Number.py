'''
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

Have you met this question in a real interview? Yes
Example
Given [1,2,2,1,3,4,3], return 4

'''
class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        res = 0
        for number in A:
            res = res ^ number
        return res
'''
Note:
1. Exclusive or produce 1 when two bits are different and 0 when they are same.
'''