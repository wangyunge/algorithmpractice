'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

The array may contain duplicates.
'''
class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        left = 0
        right = len(num)-1
        while left < right-1:
            mid = (right+left)/2
            if num[mid] == num[left] and num[mid] == num[right]:
                res = float('inf')
                for i in xrange(left,right+1):
                    res = min(num[i],res)
                return res
            if num[mid] < num[right]:
                right = mid
            elif num[mid] >= num[left]:
                left = mid
            else:
                right = mid
        return min(num[left],num[right])



