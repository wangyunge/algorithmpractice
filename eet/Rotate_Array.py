'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

'''

"""
Note:
Rotet it by reversing the arrary
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        newNums = nums[n-k:]+nums[:n-k]
        for i in xrange(n):
            nums[i] = newNums[i]
def main():
    test = [1,2,3,4,5,6,7]
    sol = Solution()
    sol.rotate(test,3)
if __name__ == '__main__':
    main()