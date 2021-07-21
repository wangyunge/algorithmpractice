class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _check2(arr):
            return sum(arr[1:]) > arr[0]
        nums = sorted(nums, reverse=True)
        for i in range(0, len(nums)-2):
            if _check2(nums[i:i+3]):
                return sum(nums[i:i+3])
        return 0

