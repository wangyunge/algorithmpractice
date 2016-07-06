'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

Subscribe to see which companies asked this question

Show Tags
'''
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #Constraint:
        #1.Less than 255. 2.Start with non-zero element.
        self.res = []
        self.s = s
        stack = []
        Depth = 0
        index =0
        self.DFS(stack,index,Depth)
        return self.res
    def DFS(self,stack,index,Depth):
        if Depth == 4:
            if index == len(self.s):
                self.res.append(".".join(stack))
            return None
        if index < len(self.s) and self.s[index] == "0":
            self.DFS(stack+["0"],index+1,Depth+1)
        else:
            for i in xrange(0,3):
                if index+i < len(self.s) and int(self.s[index:index+i+1]) <= 255:
                    self.DFS(stack+[self.s[index:index+i+1]],index+i+1,Depth+1)

def main():
    sol = Solution()
    example = "25525511135"
    res = sol.restoreIpAddresses(example)
    print res

if __name__ == '__main__':
    main()