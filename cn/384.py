import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = []
        pool = self.nums[:]
        bounder = len(pool)-1
        while bounder >= 0:
            pos = random.randint(0, bounder)
            res.append(pool[pos])
            pool[pos], pool[bounder] = pool[bounder], pool[pos]
            bounder -= 1
        return res





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
