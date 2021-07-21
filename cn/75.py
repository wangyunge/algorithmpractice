class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        fst = 0
        snd = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[fst] = nums[fst], nums[i]
                fst += 1
            if nums[i] == 1:
                nums[i], nums[snd] = nums[snd], nums[i]
                snd += 1
            snd = max(snd, fst)

