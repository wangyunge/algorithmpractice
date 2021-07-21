'''
All result,
no duplicate
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def _two_pointer(i, j, t):
            while i < j:
                if nums[i] + nums[j] == t:
                    return True, i, j
                elif nums[i] + nums[j] > t:
                    j -= 1
                else:
                    i += 1
            return False, i, j
        res = []
        nums = sorted(nums)
        for s, start in enumerate(nums):
            if s > 0 and nums[s-1] == start:
                continue
            found, left, right = _two_pointer(s+1, len(nums)-1, -nums[s])
            while found:
                res.append([nums[s], nums[left], nums[right]])
                while left+1 < len(nums) and nums[left+1] == nums[left]:
                    left += 1
                while right-1 > s and nums[right-1] == nums[right]:
                    right -= 1
                found, left, right = _two_pointer(left+1, right-1, -nums[s])
        return res

