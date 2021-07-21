class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def _dfs(idx):
            sign = 1
            num = 0
            digit = False
            res = 0
            while idx < len(s) and s[idx] != ')':
                if s[idx] == '+':
                    res += sign * num   
                    sign = 1 
                    num = 0
                    idx += 1
                elif s[idx] == '-':
                    res += sign * num   
                    num = 0
                    sign = -1
                    idx += 1
                elif s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                    idx += 1
                elif s[idx] == '(':
                    num, idx = _dfs(idx+1)
                else:
                    idx += 1
            res += sign * num   
            return res , idx+1
        res, _ = _dfs(0)
        return res 


