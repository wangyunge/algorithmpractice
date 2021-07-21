class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        table1 = {0: 1}

        table2 = {}

        for i in range(len(nums)):
            add = nums[i]
            for key, value in table1.items():

                table2.setdefault(key+add, 0)
                table2[key+add] += value
                table2.setdefault(key-add, 0)
                table2[key-add] += value
            table1 = table2
            table2 = {}
        if S in table1:
            return table1[S]
        else:
            return 0


