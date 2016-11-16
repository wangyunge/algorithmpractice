'''
Given two binary strings, return their sum (also a binary string).

Have you met this question in a real interview? Yes
Example
a = 11

b = 1

Return 100

'''
class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        longS = a if len(a) >= len(b) else b
        shortS = b if len(a) >= len(b) else a
        index = 1 
        carry = 0
        res = []
        while index <= len(longS):
            if index <= len(shortS):
                cal = int(longS[-index]) + int(shortS[-index]) + carry
            else:
                cal  = int(longS[-index]) + carry
            if cal == 0:
                add = '0'
                carry = 0
            if cal == 1:
                add = '1'
                carry = 0
            if cal == 2:
                add = '0'
                carry = 1
            if cal == 3:
                add = '1'
                carry = 1
            index += 1
            res.append(add)
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)
