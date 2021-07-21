class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def _dfs(pos):
            idx = len(pos)
            if idx == n:
                res.append(pos)
            attack_range = set()
            for i in range(idx):
                attack_range.add(pos[i])
                attack_range.add(pos[i] + (idx-i))
                attack_range_add(pos[i] - (idx-i))
            for j in range(n):
                if j not in attack_range:
                    _dfs(pos+[j])
        res = []
        _dfs(n)
        return res


