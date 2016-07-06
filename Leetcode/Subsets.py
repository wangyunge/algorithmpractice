# Given a set of distinct integers, nums, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         self.nums = sorted(nums)
#         self.res = [[]]
#         for lengthOfSet in xrange(1,len(nums)+1):
#             reStack=[]
#             self.DFS(reStack,lengthOfSet,0)
#         return self.res
#     def DFS(self,reStack,k,Lowbound):
#         if len(reStack) == k:
#             self.res.append(reStack[::-1])
#         elif len(reStack) == 0:
#             for i in xrange(0,len(self.nums)):
#                 self.DFS([self.nums[i]]+reStack,k,i+1)
#         else:
#             for i in xrange(Lowbound,len(self.nums)):
#                 self.DFS([self.nums[i]]+reStack,k,i+1)
class Solution(object):
    def subsets(self, nums):
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
        if not reStack: 
            self.res.append(reStack[::-1])
        for i in xrange(Lowbound,len(self.nums)):
            self.DFS([self.nums[i]]+reStack,i+1)


def main():

    sol = Solution()
    res = sol.subsets([0,3,2])
    print  res
if __name__ == '__main__':
    main()
