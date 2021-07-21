class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = [s[i] for i in range(len(s))]
        res = []
        def _dfs(i):
            if i == len(s)-1:
                res.append(''.join(l[:]))
            else:
                visited = set()
                for j in range(i, len(l)): # start from i to skip this position
                    if l[j] in visited: continue
                    visited.add(l[j])
                    l[i], l[j] = l[j], l[i]
                    _dfs(i+1)
                    l[i], l[j] = l[j], l[i]
        _dfs(0)
        return res

"""
Coner Case:
1. What if they have same letters
"""


class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res

