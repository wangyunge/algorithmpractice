class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        for i in range(n+1):
            pos = abs(nums[i]) - 1
            if nums[pos] < 0:
                return pos+1
            else:
                nums[pos] = -nums[pos]
        return

