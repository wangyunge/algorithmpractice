class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        B = [0]
        for i in range(len(nums)):
            B.append(B[-1] + nums[i])
        table = {}
        res = 0
        for i in range(len(B)):
            rest = B[i] - k
            if rest in table:
                res += table[rest]
            if B[i] in table:
                table[B[i]] += 1
            else:
                table[B[i]] = 1
        return res

