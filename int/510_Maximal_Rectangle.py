'''
Given a 2D boolean matrix filled with False and True, find the largest rectangle containing all True and return its area.

Have you met this question in a real interview? Yes
Example
Given a matrix:

[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
return 6.

'''
class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        DP = [[0 for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
        DP[0][0] = 1 if matrix[0][0] == 1 else 0
        for j in xrange(0,len(matrix[0])):
            DP[0][j] = matrix[0][j]
            for i in xrange(1,len(matrix)):
                if matrix[i][j] == 0:
                    DP[i][j] = 0
                else:
                    DP[i][j] = DP[i-1][j] + 1
        res = 0
        for i in xrange(0,len(DP)):
            DP[i].append(0)
            stack = [-1]
            for j in xrange(len(DP[0])):
                while DP[i][j] < DP[i][stack[-1]]:
                    lowestHight = DP[i][stack.pop()]
                    width = j - stack[-1] -1
                    res = max(res,width*lowestHight)
                stack.append(j)
        return res
def main():
    test = [[1,1,0,0,1],[0,1,0,0,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,0,1]]
    sol = Solution()
    sol.maximalRectangle(test)

if __name__ == '__main__':
    main()