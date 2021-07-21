"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.



Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.


Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k = abs(k)   # Integer 整数
        B = [0] * len(nums)

        if k == 0 :
            if len(nums) >= 2 and nums[0] ==0 and nums[1] == 0:
                return True
            else:
                return False
        tmp_sum = 0
        table = {}
        table[0] = -1 # for the sequence includes the first element
        for idx in range(len(nums)):
            tmp_sum += nums[idx]

            if tmp_sum % k in table:
                i = table[tmp_sum % k]
                if idx - table[tmp_sum % k]  > 1: # At least two numbers
                    if tmp_sum - B[i] > 0: #  check n is larger than 0
                        return True
            else:
                table[tmp_sum % k] = idx
            B[idx] = tmp_sum
        return False



class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k = abs(k)
        B = [0 for _ in range(len(nums)+1)]
        for idx in range(1,len(nums)+1):
            B[idx] = B[idx-1] + nums[idx-1]

        if k == 0 :
            if len(nums) >= 2 and nums[0] ==0 and nums[1] == 0:
                return True
            else:
                return False
        table = {}

        for idx in range(0, len(nums)+1):
            n = 0
            while k * n <= B[idx] :
                if B[idx] - k * n in table:
                    if idx - table[B[idx]-k*n] != 1:
                        return True
                n += 1
            table[B[idx]] = idx
        return False





