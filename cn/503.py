class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        res = [-1 for _ in range(L)]
        stack = []
        nums.extend(nums)
        for idx in range(2 * L):
            while stack and nums[stack[-1]] < nums[idx]:
                pos = stack.pop()
                if pos < L:
                    res[pos] = nums[idx]
            stack.append(idx)
        return res
