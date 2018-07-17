'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        if not k:
            return self.res
        if not n:
            return self.res 

        for i in xrange(1, 10):
            if i <= n:
                self.dfs([i], k-1, n - i)
        return self.res

    def dfs(self, base, k, n):
        if k == 0 and n == 0:
            self.res.append(base)
        if k > 0:
            for i in xrange(base[-1] + 1, 10):
                if i <= n:
                    self.dfs(base + [i], k-1, n-i )