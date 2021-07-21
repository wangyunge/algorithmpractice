class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []
        res = []
        carry = 1
        for num in digits[::-1]:
            tmp = num + carry
            carry = tmp // 10
            res.append(tmp%10)
        if carry:
            res.append(carry)
        return res[::-1]