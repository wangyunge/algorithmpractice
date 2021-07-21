"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)

        res = [0] * (l1 + l2 +1)

        for i in range(l1)[::-1]:
            for j in range(l2)[::-1]:
                pdc = int(num1[i]) * int(num2[j])
                plus = res[i+j] + pdc
                res[i+j] += pdc % 10
                res[i+j+1] =  pdc / 10
        res = map(res, lambda x: str(x))
        if res[0] == '0':
            return ''.join(res[1:])
        else:
            return ''.join(res)






























