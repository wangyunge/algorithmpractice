class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def _reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        l = len(nums)
        # l < k
        k = k % l
        _reverse(0, l-1)
        _reverse(0, k-1)
        _reverse(k, l-1)

