'''
Implement int sqrt(int x).

Compute and return the square root of x.

Have you met this question in a real interview? Yes
Example
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3
'''
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        left = 0
        right = x
        while left < right-1:
        	mid = (left+right)/2
        	if mid*mid == x:
        		return mid
        	if mid*mid > x:
        		right = mid
        	else:
        		left = mid
        if right*right == x:
        	return right
        else:
        	return left