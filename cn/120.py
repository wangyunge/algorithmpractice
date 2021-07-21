class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = triangle[:]
        for i in range(1, len(triangle)):
            res[i][0] += res[i-1][0]
            res[i][len(res[i])-1] += res[i-1][len(res[i-1])-1]
            for j in range(1, len(triangle[i])-1):
                res[i][j] += min(res[i-1][j-1], res[i-1][j])
        return min(res[-1])



