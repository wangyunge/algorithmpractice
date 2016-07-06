'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums)-1
        

        while L <= R:
            mid = (L+R)/2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] >= nums[L]:
                    if nums[L] <= target <= nums[mid]:
                        R = mid-1
                    else:
                        L = mid+1
                elif nums[mid] <= nums[R]:
                    if nums[mid] <= target <= nums[R]:
                        L = mid +1
                    else:
                        R = mid-1
                else:
                    break

        return -1
def main():
    sol = Solution()
    res = sol.search([3,1],1)
    print  res
if __name__ == '__main__':
    main()
        