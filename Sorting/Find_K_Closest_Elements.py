"""
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
Absolute value of elements in the array and x will not exceed 104
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = start + k 
        abs_sum = 0
        for idx in range(start, end):
            abs_sum += abs(x - arr[idx])
        min_sum = abs_sum
        res = [start, end]
        while end < len(arr) :
            abs_sum -= abs(x - arr[start])
            abs_sum += abs(x - arr[end])
            start += 1
            end += 1
            if abs_sum < min_sum:
                res = (start, end)
        return arr[res[0]:res[1]]
"""
Notes:
x - A[mid-*] > x-A[mid] > A[mid+k] - x > A[mid+k-*]-x

x - A[mid+*] < x -A[mid] < A[mid+k]- x < A[mid+k+*]-x
"""