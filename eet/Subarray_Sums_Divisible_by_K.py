"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.



Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""

class Solution(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)/2 for v in count.values())

"""
Note:

prefix sum: Same to
Continuous Subarray Sum.

Let there be a subarray (i, j) whose sum is divisible by k
  sum(i, j) = sum(0, j) - sum(0, i-1)
Sum for any subarray can be written as q*k + rem where q
is a quotient and rem is remainder
Thus,
    sum(i, j) = (q1 * k + rem1) - (q2 * k + rem2)
    sum(i, j) = (q1 - q2)k + rem1-rem2

We see, for sum(i, j) i.e. for sum of any subarray to be
divisible by k, the RHS should also be divisible by k.
(q1 - q2)k is obviously divisible by k, for (rem1-rem2) to
follow the same, rem1 = rem2 where
    rem1 = Sum of subarray (0, j) % k
    rem2 = Sum of subarray (0, i-1) % k
"""


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        B = [0 for _ in range(len(A)+1)]
        table = {0: 1}
        res = 0
        for idx in range(1, len(A)+1):
            B[idx] = A[idx-1] + B[idx-1]
            rem = B[idx] % k
            if rem in table:
                res += table[rem]
                table[rem] += 1
            else:
                table[rem] = 1
        return res


