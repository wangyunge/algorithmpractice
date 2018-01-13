'''
Given a set of distinct integers, return all possible subsets.

 Notice

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Have you met this question in a real interview? Yes
Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        self.s = sorted(S)
        self.res = [[]]
        for i in xrange(len(self.s)):
            self.res.append([self.s[i]])
            self.DFS(i+1,[self.s[i]])
        return self.res
    def DFS(self,index,pack):
        for i in xrange(index,len(self.s)):
            self.res.append(pack+[self.s[i]])
            self.DFS(i+1,pack+[self.s[i]])
