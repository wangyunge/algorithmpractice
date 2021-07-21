'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return 

        # Ierate every items
        for pi in range(len(nums)):
            # pi which is the index = i th number -1. i is the position of the number.
            if pi == nums[pi]-1:
                continue
            else:
                idx = nums[pi]-1
                # Set nums[idx] = idx and build a linked list
                while idx >= 0 and idx != nums[idx]-1:
                    idx_next = nums[idx]-1
                    nums[idx] = idx+1
                    idx = idx_next

        # Check which number has not been pointed to 
        res = []
        for pi in range(len(nums)):
            if pi != nums[pi]-1:
               res.append(pi + 1)

        # return 0 if there is not missing number. 
        # Corner case
        return res
