"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1)[::-1]:
            # Find the switch point
            if nums[i] < nums[i+1]:
                # switch the bottom
                for j in range(i, len(nums)-1):
                    if nums[i] > nums[j+1]:
                        break
                    nums[j], nums[i] = nums[i], nums[j]
                    # Sort the tail asc to make it smallest
                    nums[i+1:] = sorted(nums[i+1:])
"""
1. Conner Case: the last of the series
2. Sort is not necessay as the tail is ordered.
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        povit = len(nums) - 1

        while povit > 0 and nums[povit-1] >= nums[povit]:
            povit -= 1

        if povit != 0:

            swap = len(nums) - 1
            while swap >= povit:
                if nums[swap] > nums[povit-1]:
                    nums[swap], nums[povit-1] =  nums[povit-1], nums[swap]
                    break
                else:
                    swap -= 1

        swap = len(nums) - 1
        while povit < swap:
            nums[povit], nums[swap] = nums[swap], nums[povit]
            povit += 1
            swap -= 1



"""
Note:
Conner case: start over for biggest num.
"""
