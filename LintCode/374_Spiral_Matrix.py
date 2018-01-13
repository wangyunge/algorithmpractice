'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Have you met this question in a real interview? Yes
Example
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
		if not matrix:
			return []
		i=0
		j=0
		mi=0
		mj=0
		res = [matrix[0][0]]
		direction = "right"
		Done = False
		DoneDone = False
		while wall > 2:
			if direction == "right":
				if j+1 < len(matrix[0]) and matrix[i][j+1] != "#":
					wall = 1
					res.append(matrix[i][j+1])
					matrix[i][j+1] = "#"
					mi = i
					mj = j+1
				else:
					wall += 1
					direction == "down"
			elif direction == "down":
				if i+1 < len(matrix) and matrix[i+1][j] != "#":
					res.append(matrix[i+1][j])
					matrix[i+1][j] = "#"
					mi = i+1
					mj = j
				else:
					direction = "left"
			elif direction == "left":
				if j-1>=0 and matrix[i][j-1] != "#":
					res.append(matrix[i][j-1])
					matrix[i][j-1] = "#"
					mi = i
					mj = j-1
				else:
					direction = "up"
			elif direction == "up":
				if i-1 >= 0 and matrix[i-1][j] != "#":
					res.append(matrix[i-1][j])
					matrix[i-1][j]
					mi = i-1
					mj =j
			if mi == i and mj == j:
				return res
			else:
				i = mi
				j = mj

