'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Have you met this question in a real interview? Yes
Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.s = s
        self.res = []
        for j in xrange(len(s)):
            if self.isPalindrome(0,j):
                self.DFS([s[:j+1]],j+1)
        return self.res
    def isPalindrome(self,left,right):
        while left < right:
            if self.s[left] != self.s[right]:
                return False
            left += 1
            right -= 1
        return True
    def DFS(self,pack,start):
        if start == len(self.s):
            self.res.append(pack)
        else:
            for j in xrange(start,len(self.s)):
                if self.isPalindrome(start,j):
                    self.DFS(pack+[self.s[start:j+1]],j+1)

