'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Have you met this question in a real interview? Yes
Example
Given "25525511135", return

[
  "255.255.11.135",
  "255.255.111.35"
]
Order does not matter.
'''
class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        self.s = s
        start = 0
        self.res = []
        if not s:
            return []
        if self.s[0] == '0':
            self.DFS('0',1,1)
        else:
            for i in xrange(start+1,len(self.s)+1):
                if int(self.s[start:i]) <= 255:
                    self.DFS(self.s[start:i],i,1)
                else:
                    break
        return self.res
    def DFS(self,res,start,dot):
        if start == len(self.s) and dot == 4:
            self.res.append(res)
        elif start != len(self.s) and dot != 4:
            if self.s[start] == '0':
                self.DFS(res +'.0',start+1,dot+1)
            else:
                for i in xrange(start+1,len(self.s)+1):
                    if int(self.s[start:i]) <= 255:
                        self.DFS(res+'.'+self.s[start:i],i,dot+1)
                    else:
                        break