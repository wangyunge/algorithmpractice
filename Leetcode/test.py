class Solution:
    """
    1. Difference to Find the Duplicate Number is that we can change the number in place.
    """
    def findDuplicates(self, nums) :
        res = []
        for pi in range(len(nums)):
            if nums[pi] < 0: 
                continue
            idx = nums[pi] - 1
            while idx >= 0 and idx != nums[idx] -1: 
                ne_idx = nums[idx] -1
                nums[idx] = -(idx + 1)
                if nums[ne_idx] < 0:
                    res.append(-nums[ne_idx])
                    break
                idx = ne_idx
        return res


def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    nums = [4,3,2,7,8,2,3,1]

    ret = Solution().findDuplicates(nums)

    out = intToString(ret)

    print(out)

if __name__ == '__main__':
    main()    

