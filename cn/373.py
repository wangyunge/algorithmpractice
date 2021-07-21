class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        table = {}
        ma = a % 1337
        table[ma] = 0
        # Get Circle
        mul = 1
        for i in range(1, 1337):
            mul = mul * ma % 1337
            if mul in table:
                break
            else:
                table[mul] = i
        L = i

        # b % L
        base_mode = 1
        pos = 0
        for j, num in enumerate(b):
            pos = pos + num % L * base_mode
            base_mode = base_mode * ( 10 % L ) % L
        return table[pos]

