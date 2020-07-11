'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''
class Solution:
    """
    Cycle Detection. 
    1. The in-degree of a node(idx = number = address of node) equals the times a number appear (pointed to)
    2. Cycle means one node is pointed to more than once(in-degree bigger than 1). Positin 0 is the start and only contributes to in-degree. 
    """
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 
            
        # First meet
        slow = 0
        fast = nums[0]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Second meet 
        snd = 0
        slow = nums[slow]

        while slow != snd:
            slow = nums[slow]
            snd = nums[snd]
        
        return snd 