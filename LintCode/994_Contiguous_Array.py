'''
Description
中文
English
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

The length of the given binary array will not exceed 50,000.

Have you met this question in a real interview?  
Example
Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1
'''
class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        if not nums:
            return 
        res = 0
        counter = 0
        cnt_dict = {0:-1}
        for idx in range(len(nums)):
            counter += 1 if nums[idx] == 1 else -1
            if counter not in cnt_dict:
                cnt_dict[counter] = idx
            else:
                res = max(res, idx - cnt_dict[counter])
        return res 
'''
Note:
1. Use the Counter as Water Level. Water is usefull in array problems.
2. The position of water level 0 is -1
3. The left end of horizontal line has been counted before, So we should exclude it. 
