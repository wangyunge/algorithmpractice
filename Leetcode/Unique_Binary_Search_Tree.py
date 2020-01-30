'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [1, 1]
        for m in range(2, n+1):
            res_m = 0
            for mid in range(m):
                res_m += DP[mid] * DP[m-mid-1]  
            DP.append(res_m)
        return DP[-1]
