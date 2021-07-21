class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i, item in enumerate(nums):
            if item not in table:
                table[item] = i
            else:
                if i - table[item] <= k:
                    return True 
                else:
                    table[item] = i 
        return False 