'''
1. range(len(nums)-1, -1 , -1)
2. pos refere before asign
3. deal with end situation
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # povit
        pos = -1
        for i in range(len(nums)-2, -1 , -1):
            if nums[i] < nums[i+1]:
                pos = i
                break
        if pos != -1:
            # min bigger than povit
            for i in range(len(nums)-1, pos, -1):
                if nums[i] > nums[pos]:
                    swap = i
                    break
            nums[pos], nums[swap] = nums[swap], nums[pos]
        # asc
        l = pos + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1




