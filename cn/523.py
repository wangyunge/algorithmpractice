class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        B = 0
        table = {B:-1}
        for i in range(len(nums)):
            B = B + nums[i]

            offset = B % k
            if offset in table:
                if i - table[offset] > 1:
                    return True
            else:
                table[offset] = i
        return False


