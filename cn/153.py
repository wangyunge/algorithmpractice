class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        # ascend
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:

            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1

        return nums[l]

