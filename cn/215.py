class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def _partition(l, r):
            pos = l
            for i in range(l+1, r+1):
                if nums[i] >= nums[l]:
                    pos += 1
                    nums[pos], nums[i] = nums[i], nums[pos]
            nums[pos], nums[l] = nums[l], nums[pos]
            return pos

        l = 0
        r = len(nums) - 1
        k = k-1
        while 1:
            pos = _partition(l, r)
            if pos > k:
                r = pos-1
            elif pos < k:
                l = pos+1
            else:
                break
        return nums[pos]
