'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Have you met this question in a real interview? Yes
Example
Given [3, 8, 4], return 8.

'''
class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        if not A:
            return 0
        DP = [[0,0] for i in xrange (len(A))]
        DP[0][0] = 0
        DP[0][1] = A[0]
        for i in xrange(1,len(A)):
            DP[i][0] = max(DP[i-1])
            DP[i][1] = DP[i-1][0] + A[i]
        return max(DP[len(A)-1])