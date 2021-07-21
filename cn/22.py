class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def _dfs(cnt, single, path):
            if cnt == n and single == 0:
                res.append(''.join(path))
            else:
                if cnt < n:
                    _dfs(cnt+1, single+1, path + ['('])
                if single > 0:
                    _dfs(cnt, single-1, path + [')'])
        res = []
        _dfs(0, 0, [])
        return res




