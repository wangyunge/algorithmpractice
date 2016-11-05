'''
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

 Notice

You may assume that the array is non-empty and the majority number always exist in the array.
'''
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        counts = 0
        res = nums[0]
        counts = 1
        for i in xrange(1,len(nums)):
            if nums[i] == res:
                counts +=1
            else:
                if counts == 1:
                    res = nums[i]
                else:
                    counts -= 1
        return res