'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i]  num[i+1], find a peak element and return its index
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = 

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.
'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peaks = []
        length = len(nums)
        for i in xrange(length):
            if i==0:
                if i+1 < length and nums[i] > nums[i+1]:
                    return i
            elif i == length-1:
                if i-1 > 0 and nums[i-1] < nums[i]:
                    return i
            else:
                if nums[i-1] < nums[i]  and nums[i+1] < nums[i]:
                    return i
        return None 
def main():
    sol = Solution()
    text = [1,2]
    res = sol.findPeakElement(text)

if __name__ == '__main__':
    main()