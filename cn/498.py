class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        M = len(matrix) - 1
        N = len(matrix[0]) - 1
        res = []
        for add in range(M+N+1):
            if add % 2 == 0:
                i = min(M, add)
                while i >= 0 and add-i <= N  :
                    res.append(matrix[i][add-i])
                    i -= 1
            else:
                j = min(N, add)
                while j >= 0 and add-j <= M:
                    res.append(matrix[add-j][j])
                    j -= 1
        return res



