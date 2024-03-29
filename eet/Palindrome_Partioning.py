'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp = [[]for _ in range(s)]
        # dp[0] = s[0]
        dp = [s[0]]
        for idx in range(1,len(s)):
            tmp = []
            for last_list in dp:
                if _check(last_list[-1]+s[idx]):
                    tmp.append(last_list[:-1] + [last_list[-1] + s[idx]])
                if len(last_list) > 1 and last_list[-2] == s[idx]:
                    tmp.append(last_list[:-2] + [''.join(last_list[-2:] + s[idx])])
                tmp.append(last_list + [s[idx]])

            dp = tmp
        return dp




class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        self.s = s
        self.res = []
        self.DFS(0,[])
        return self.res

    def DFS(self,index,pack):
        if index == len(self.s)-1:
            self.res += pack
        else:
            for i in xrange(index,len(self.s)):
                if self.isPalindrome(index,i):
                    self.DFS(i,pack+[self.s[index:i+1]])

    def isPalindrome(self,l,r):
        res = True
        while l<=r:
            if self.s[l] != self.s[r]:
                res = False
                break
            l += 1
            r -= 1
        return res
def main():
    sol = Solution()
    test = "aab"
    res = sol.partition(test)
if __name__ == '__main__':
    main()
