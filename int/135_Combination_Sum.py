'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.



For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

 Notice

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Have you met this question in a real interview? Yes
Example
given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3]
'''
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.candidates = []
        for i in xrange(len(candidates)):
            if i == 0 or candidates[i] != self.candidates[-1]:
                self.candidates.append(candidates[i])
        self.target = target
        self.res = []
        for i in xrange(len(self.candidates)):
            self.DFS(i,[self.candidates[i]],self.candidates[i])
        return self.res
    def DFS(self,index,resSoFar,sumSoFar):
        if sumSoFar == self.target:
            resSoFar.sort()
            self.res.append(resSoFar)
        if sumSoFar < self.target:
            for i in xrange(index,len(self.candidates)):
                self.DFS(i,resSoFar+[self.candidates[i]],sumSoFar+self.candidates[i])