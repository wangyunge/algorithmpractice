class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # interger part
        int_part = numerator // denominator
        table = {}
        dci = numerator % denominator
        res = []
        i = 0
        while dci != 0:
            if dci in table:
                break
            table[dci] = i
            dci *= 10
            res.append(str(dci // denominator))
            i += 1
            dci = dci % denominator
        if dci == 0:
            if res:
                return str(int_part) + '.' + ''.join(res)
            else:
                return str(int_part)
        else:
            pos = table[dci]
            return str(int_part)+ '.' + ''.join(res[:pos]) + '(' + ''.join(res[pos:]) + ')'




