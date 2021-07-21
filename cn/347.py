class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ladder = [[] for _ in range(len(nums))]
        table = {}
        for item in nums:
            if item not in table:
                table[item] = 0
            else:
                table[item] += 1
            ladder[table[item]].append(item)
        cnt = 1
        res = []
        for i in range(len(nums)-1, -1, -1):
            if cnt > k:
                break
            for item in ladder[i]:
                if table[item] == i:
                    res.append(item)
                    cnt +=1
        return res

