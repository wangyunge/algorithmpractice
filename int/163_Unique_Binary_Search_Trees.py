'''
Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

Have you met this question in a real interview? Yes
Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3
'''
class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        DP = [1 for i in xrange(n+1)]
        dpIndex = 1
        while dpIndex <= n:
        	tmpRes = 0
        	for i in xrange(1,dpIndex+1):
        		tmpRes += DP[i-1]*DP[dpIndex-i]
        	DP[dpIndex] = tmpRes
        	dpIndex += 1
        return DP[n]