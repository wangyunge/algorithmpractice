class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        table = {}
        top = 0
        for char in S:
            table.setdefault(char, 0)
            table[char] += 1
            top = max(top, table[char])
        if top > (len(S)+1)//2:
            return None
        order = sorted(table.items(), key=lambda x: x[1], reverse=True)
        res = [''] * len(S)
        step = 0
        j = -1
        for i in range(0, len(S), 2):
            if step < 1:
                j+=1
                step = order[j][1]
            res[i] = order[j][0]
            step -= 1
        for i in range(1, len(S), 2):
            if step < 1:
                j+=1
                step = order[j][1]
            res[i] = order[j][0]
            step -= 1
        return ''.join(res)


