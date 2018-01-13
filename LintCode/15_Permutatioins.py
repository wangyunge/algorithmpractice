'''
Given a list of numbers, return all possible permutations.

 Notice

You can assume that there is no duplicate numbers in the list.

Have you met this question in a real interview? Yes
Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
    	if not nums:
    		return []
    	self.nums = nums
    	self.res = []
    	for i in nums:
    		self.DFS([i])
    	return self.res
    def DFS(self,prix):
    	if len(prix) == len(self.nums):
    		self.res.append(prix)
    	else:
    		for i in self.nums:
    			if i not in prix:
    				self.DFS(prix+[i])