"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        even = 0
        odds = 0
        tmp = 1
        for i in range(34):
            if i % 2 == 0:
                even += tmp
            if i % 2 == 1:
                odds += tmp
            tmp = tmp * 2
        res = [0 for _ in range(len(num))]
        for i in range(len(num)):
            a = even & item
            b = odds & item
            res[i] = res[a] + res[b]
        return res
"""
Notes:
Dynamic Programming:
Current numbers has one more 1 than the one minus the highest postion 1000
1 1101 -- 0 1101
1 0001 -- 0 0001
"""
0
1 res[0] +1    01
2 res[0] + 1    10
3 res[1] + 1
4 res[2] + 1
5
6
7
8


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        k = 0
        idx = 1
        res = [0] * num
        res[1] = 1
        while idx <= num:
            offset = 0
            while idx < pow(2,k+1):
                res[idx] = res[idx-pow(2,k)] + 1
                idx += 1
                offset += 1
            k += 1
        return res





