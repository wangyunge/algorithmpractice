'''
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

 Notice

The list may contains duplicate integers.

Have you met this question in a real interview? Yes
Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]

'''
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        Descending = True
        for i in range(len(num)-1)[::-1]:
            if num[i] < num[i+1]:
                Descending = False
                break
        if Descending:
            num.reverse()
            return num
 
        for l in range(i,len(num))[::-1]:
            if num[l] > num[i]:
                break
        num[i],num[l] = num[l],num[i]
        num[i+1:] = sorted(num[i+1:])
        return num
