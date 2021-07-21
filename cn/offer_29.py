class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        top = 0
        left = 0
        right = len(matrix[0]) - 1  # Empty
        bottom =  len(matrix) - 1
        i = 0
        j = 0
        res = []
        while top <= bottom or left <= right:
            while left <= i and i <= right  :
                res.append(matrix[j][i])
                i += 1
            i = right
            top += 1
            j  = top
            while top <= j and j <= bottom:
                res.append(matrix[j][i])
                j += 1
            j = bottom
            right -= 1
            i = right
            while right >= i and  i >= left:
                res.append(matrix[j][i])
                i -= 1
            i = left
            bottom -= 1
            j = bottom
            while bottom >= j and  j >= top:
                res.append(matrix[j][i])
                j -= 1
            j = top
            left += 1
            i = left
        return res 
                
