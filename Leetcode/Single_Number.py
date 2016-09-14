'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for integers in nums:
            if integers not in dic:
                dic[integers] = 1
            else:
                dic[integers] +=1
        for integers,times in dic.iteritems():
            if times == 2:
                return integers
        return None
    def singleNumber(self,nums):
        x = 0 
        for i in nums:
            x = x^i

        return x