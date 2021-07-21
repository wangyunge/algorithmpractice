'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

Have you met this question in a real interview? Yes
Example
For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.

'''
class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        res = nums[0]
        posMax = nums[0]
        negMax = nums[0]
        for i in xrange(1,len(nums)):
            if nums[i] < 0:
                posMax,negMax = negMax,posMax
            
            posMax = max(nums[i],posMax*nums[i])
            negMax = min(nums[i],negMax*nums[i])
            res = max(res,posMax)
        return res