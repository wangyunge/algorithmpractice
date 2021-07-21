"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        fst = 0
        snd = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[fst], nums[snd], nums[i] = nums[i], nums[fst], nums[snd]
                fst += 1
                snd += 1
            elif nums[i] == 1:
                nums[snd], nums[i] = nums[i], nums[snd]
                snd += 1





"""
Note:
Three way partition
"""
# Partitions arr[0..n-1] around [lowVal..highVal]
def threeWayPartition(arr, n, lowVal, highVal):

    # Initialize ext available positions for
    # smaller (than range) and greater lements
    start = 0
    end = n - 1
    i = 0

    # Traverse elements from left
    while i <= end:

        # If current element is smaller than
        # range, put it on next available smaller
        # position.
        if arr[i] < lowVal:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            i += 1
            start += 1

        # If current element is greater than
        # range, put it on next available greater
        # position.
        elif arr[i] > highVal:
            temp = arr[i]
            arr[i] = arr[end]
            arr[end] = temp
            end -= 1

        else:
            i += 1
