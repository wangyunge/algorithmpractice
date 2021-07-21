class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        B1 = nums[:]
        for i in range(1, len(nums)):
            B1[i] = nums[i] * B1[i-1]


        B2 = nums[:]
        for j in range(len(nums)-2, -1, -1):
            B2[j] = nums[j] * B2[j+1]
        res = nums[:]

        for k in range(len(nums)):
            if k == 0:
                res[k] = B2[k+1]
            elif k == len(nums)-1:
                res[k] = B1[k-1]
            else:
                res[k] = B1[k-1]*B2[k+1]
        return res


