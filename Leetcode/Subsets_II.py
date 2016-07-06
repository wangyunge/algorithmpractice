'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = sorted(nums)
        self.res = [[]]
        reStack=[]
        self.DFS(reStack,0)
        return self.res
    def DFS(self,reStack,Lowbound):
        if reStack: 
            self.res.append(reStack[::-1])
        for i in xrange(Lowbound,len(self.nums)):
            if i==0:
                self.DFS([self.nums[i]]+reStack,i+1)
            elif self.nums[i-1] != self.nums[i]:
                self.DFS([self.nums[i]]+reStack,i+1)
            elif i == Lowbound:
                self.DFS([self.nums[i]]+reStack,i+1)
def main():

    sol = Solution()
    res = sol.subsetsWithDup([1,2,2])
    print  res
if __name__ == '__main__':
    main()
