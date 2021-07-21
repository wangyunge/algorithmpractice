class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = l + (r-l) /2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[r] and nums[mid] == nums[l]:
                if target > nums[mid]:
                    l = l + 1
                else:
                    r = r - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
