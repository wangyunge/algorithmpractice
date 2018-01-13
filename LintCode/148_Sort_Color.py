'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

 Notice

You are not suppose to use the library's sort function for this problem. 
You should do it in-place (sort numbers in the original array).

Have you met this question in a real interview? Yes
Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].
'''
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        pos = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                nums[i],nums[pos] = nums[pos],nums[i]
                pos += 1
        for i in xrange(pos,len(nums)):
            if nums[i] == 1:
                nums[i],nums[pos] = nums[pos],nums[i]
                pos += 1
