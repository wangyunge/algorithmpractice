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
    def findClosestElements(self, arr, k, x) :
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
                min_sum = abs_sum
        return arr[res[0]:res[1]]


class Solution:
    def findClosestElements(self, arr, k, x) :
        start = 0
        end = start + k -1 
        l = 0
        r = len(arr) - k 
        while l < r:
            mid = (l+r)//2
            start = mid
            end = start + k -1
            if abs(x - arr[start-1]) < abs(x-arr[end]):   # This would go wrong when arr[start] == arr[end+1] or arr[start-1] == arr[end]
                r = mid
            elif abs(x - arr[start]) > abs(x-arr[end+1]):
                l = mid 
            else:
                return sum(arr[start:end+1])
"""
1.
x - A[mid-*] > x-A[mid] > A[mid+k] - x > A[mid+k-*]-x

x - A[mid+*] < x -A[mid] < A[mid+k]- x < A[mid+k+*]-x

2. 
Why not use abs()
If A[mid] == A[mid + k], we do not know whether we should move left or right when checking the absolute value.
So, if you really want to use abs, add logic for arr[mid] == arr[mid + k], eg:

if (arr[mid] == arr[mid + k]) {  // <---- add this
    if (x > arr[mid])
        left = mid + 1;
    else
        right = mid;
} else if (Math.abs(arr[mid]-x) > Math.abs(arr[mid+k]-x))
    left = mid + 1;
else
    right = mid;
Ref:  https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
"""
