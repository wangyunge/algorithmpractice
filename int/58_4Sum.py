'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

 Notice

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

Have you met this question in a real interview? Yes
Example
Given array S = {1 0 -1 0 -2 2}, and target = 0. A solution set is:

(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)
'''
class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        res = []
        numbers.sort()
        for i in xrange(len(numbers)):
            if i != 0 and numbers[i] == numbers[i-1]:
                continue
            for j in xrange(i+1,len(numbers)):
                if numbers[j] == numbers[j-1] and j>i+1:
                    continue
                h = j+1
                k = len(numbers)-1
                while h<k:
                    s = numbers[i]+numbers[j]+numbers[h]+numbers[k]
                    if s > target:
                        k-=1
                    elif s < target:
                        h+=1
                    else:
                        res.append((numbers[i],numbers[j],numbers[h],numbers[k]))
                        while h<k and numbers[h] == numbers[h+1]:
                            h+=1
                        while h<k and numbers[k] == numbers[k-1]:
                            k-=1
                        h+=1
                        k-=1
        return res