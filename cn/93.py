class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def _dfs(idx, path):
            if idx == len(s) and len(path) == 4:
                res.append('.'.join(path))
            else:
                for i in range(idx, min(len(path), idx+3)):
                    if i == idx:
                        _dfs(i+1, path+[s[i]])
                    else:
                        num = s[idx:i+1]
                        if num >= '10' and num <= '255':
                            _dfs(i+1, path + [num])
        res = []
        _dfs(0,[])
        return res



