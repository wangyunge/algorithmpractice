'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmpMax=tmpMin=res = nums[0]
        for num in nums[1:]:
            tmpMax,tmpMin = max(num,num*tmpMax,num*tmpMin),min(num,num*tmpMax,num*tmpMin)
            res = max(res,tmpMax)
        return res