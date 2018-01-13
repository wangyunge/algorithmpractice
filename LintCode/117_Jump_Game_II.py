'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Have you met this question in a real interview? Yes
Example
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if not A:
            return 0
        index = 0
        reached = 0
        step = 0
        while index <= reached:
            reached = max(index+A[index])
            reached = reached if reached < len(A) else len(A)-1
            
    def jump(self,A):
        if not A:
            return 0

