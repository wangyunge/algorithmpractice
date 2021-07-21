'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

 Notice

You may assume that each input would have exactly one solution.

Have you met this question in a real interview? Yes
Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        res = float('inf')
        thSum = float('inf')
        numbers.sort()
        for first in xrange(len(numbers)-2):
            newT = target - numbers[first]
            second = first+1
            third = len(numbers)-1
            while second < third:
                if abs(target -(numbers[first]+numbers[second]+numbers[third])) < res:
                    res = abs(target -(numbers[first]+numbers[second]+numbers[third]))
                    thSum = (numbers[first]+numbers[second]+numbers[third])
                if numbers[second] + numbers[third] > newT:
                    third -= 1
                elif numbers[second] + numbers[third] < newT:
                    second += 1
                else:
                    break
            if thSum == 0:
                break
        return thSum
def main():
    test = [1,2,33,23,2423,33,23,1,7,6,8787,5,33,2,3,-23,-54,-67,100,400,-407,-500,-35,-8,0,0,7,6,0,1,2,-56,-89,24,2]
    sol = Solution()
    sol.threeSumClosest(test,148)
if __name__ == '__main__':
    main()