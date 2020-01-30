'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, find the sequence of gray code. A gray code sequence must begin with 0 and with cover all 2n integers.

 Notice

For a given n, a gray code sequence is not uniquely defined.

[0,2,3,1] is also a valid gray code sequence according to the above definition.

Have you met this question in a real interview? Yes
Example
Given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
'''
class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        init = [0 for i in xrange(n)]
        self.res = [0]
        self.visited = set([0])
        self.DFS(init)
        return self.res
    def DFS(self,newCode):
        for i in xrange(len(newCode)):
            newCode[i] = 1 if newCode[i] == 0 else 0
            newRes = self.bi2de(newCode)
            if newRes not in self.visited:
                self.visited.add(newRes)
                self.res.append(newRes)
                self.DFS(newCode)
                break
            else:
                newCode[i] = 1 if newCode[i] == 0 else 0
    def bi2de(self,binary):
        res = 0
        binary.reverse()
        for i in xrange(len(binary)):
            res += binary[i]*pow(2,i)
        return res

class Solution2:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return [0, 1]
        else:
            last_res = self.gray(n-1)
            last_reverse = last_res[::-1]
        for ind in range(len(last_res)) :
            last_res[ind] = 
        
