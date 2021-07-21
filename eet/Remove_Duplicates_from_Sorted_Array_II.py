'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i=0
#         for n in nums:
#             if i <2 or n > nums[i-2]:
#                 nums[i]=n
#                 i+=1
#         return i

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        pos = 0
        for idx in range(len(nums)):
            if pos < 2 or nums[idx] > nums[pos-2]:
                nums[pos] = nums[idx]
                pos += 1
        return pos



def main():
    nums = [1,1,1,2]
    sol = Solution()
    res = sol.removeDuplicates(nums)
    print res
if __name__ == '__main__':
    main()

