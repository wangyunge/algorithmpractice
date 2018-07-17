class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) <= 2:
            return max(nums)
        DA = [None] * len(nums)
        DB = [None] * len(nums)
        DA[0] = nums[0]
        DA[1] = max(nums[0], nums[1])
        for index in xrange(2, len(nums)):
            DA[index] = max(DA[index-1], DA[index-2] + nums[index])

        DB[0] = 0
        DB[1] = nums[1]
        for index in xrange(2, len(nums)):
            DB[index] = max(DB[index-1], DB[index-2] + nums[index])

        return max(DA[-2], DB[-1])

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    nums = [1,2,3,1]

    ret = Solution().rob(nums)

    out = intToString(ret)

    print out

if __name__ == '__main__':
    main()    

