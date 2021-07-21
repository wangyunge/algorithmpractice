'''
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

 Notice

The sequence of integers will be represented as a string.

Have you met this question in a real interview? Yes
Example
Given n = 5, return "111221".

'''
class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        i=1
        last = '1'
        while i < n:
            i+=1
            tmp = ''
            count = 1
            lastChar = ''
            for num in last:
                if num == lastChar:
                    count +=1
                elif lastChar != '':
                    tmp = tmp + str(count) + lastChar
                    lastChar = num
                    count = 1
                else:
                    lastChar = num
            tmp = tmp + str(count) + lastChar
            last = tmp
        return last