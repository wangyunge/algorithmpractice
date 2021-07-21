class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        zeros = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                if not flag:
                    flag = True 
                else:
                    gap = nums[i] - nums[i-1] - 1
                    if gap != -1 and gap <= zeros:
                        zeros -= gap 
                    else:
                        return False 
        return True 
"""
[0, 0, 1, 2, 5]
[0, 1, 3, 5, 6]
[0, ]
"""



