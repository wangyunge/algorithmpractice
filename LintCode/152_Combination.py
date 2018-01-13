'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Have you met this question in a real interview? Yes
Example
For example,
If n = 4 and k = 2, a solution is:
[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
'''
class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        self.res = []
        self.n = n
        if k < 0:
            return self.res
        for i in xrange(1,n+1):
            self.DFS(i+1,[i],k-1)
        return self.res
    def DFS(self,start,pack,k):
        if k == 0:
            self.res.append(pack)
        else:
            for i in xrange(start,self.n+1):
                self.DFS(i+1,pack+[i],k-1)