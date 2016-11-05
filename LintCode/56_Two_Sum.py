'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

 Notice

You may assume that each input would have exactly one solution

Have you met this question in a real interview? Yes
Example
numbers=[2, 7, 11, 15], target=9

return [1, 2]
'''
'''
Note:
    Answer is not zero-based
'''
class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        table = {}
        for i in xrange(len(numbers)):
            lookup = target-numbers[i]
            if lookup in table:
                return [table[lookup]+1, i+1]
            else:
                table[numbers[i]] = i
        return [0.0]