# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

class Solution(object):
    def DFS(self,resStack,n,k,ans):
        if len(resStack) == k:
            ans.append(resStack)
        elif len(resStack) == 0:
            for i in xrange(1,n+1):
                self.DFS(resStack+[i],n,k,ans)
        else:
            for i in xrange(resStack[-1]+1,n+1):

                self.DFS(resStack+[i],n,k,ans)
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        resStack=[]
        self.DFS(resStack,n,k,ans)
        return ans




def main():

    sol = Solution()
    res = sol.combine(10,2)
    print  res
if __name__ == '__main__':
    main()
