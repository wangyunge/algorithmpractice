'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Have you met this question in a real interview? Yes
Example
Given a matrix

[
  [1,2],
  [0,3]
],
return
[
[0,2],
[0,0]
]
'''
class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        if not matrix:
            return
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    for a in xrange(len(matrix)):
                        matrix[a][j] = '#' if matrix[a][j]!= 0 else 0
                    for b in xrange(len(matrix[0])):
                        matrix[i][b] = '#' if matrix[i][b] !=0 else 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
def main():
    test = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
    sol = Solution()
    sol.setZeroes(test)
if __name__ == '__main__':
    main()