"""
Little nine has an integer array of length 
n
n, each number in it is between 
l
l and 
r
r，and the sum of this array is divisible of 
3
3.
Please help Little nine figure out how many different possibilities this array has.
The output should 
m
o
d
1
0
9
+
7
mod10
​9
​​ +7


Example
Input：
n = 2
l = 1
r = 3
Output：
3
"""
class Solution:
    """
    @param n: the length of the array.
    @param l: the least limit for element.
    @param r: the largest limit for element.
    @return: return the ways to restore the array.
    """
    def restoreArray(self, n, l, r):
        # write your code here.

