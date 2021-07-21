class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        L = len(num1) + len(num2)
        res = [0 for _  in range(L)]
        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j]) + res[i+j]
                res[i+j] = mul % 10
                res[i+j+1] += mul // 10
        stack = []
        ishead = True
        while res:
            num = res.pop()
            if num or not ishead:
                ishead = False
                stack.append(str(num))
        if not stack:
            return '0'
        return ''.join(stack)