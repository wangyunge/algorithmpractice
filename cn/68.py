class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        rack = []
        len_list = []
        l = 0
        for item in words:
            if l + len(item) > maxWidth:
                res.append(rack)
                rack = [item]
                l = len(item) + 1
            else:
                rack.append(item)
                l = l + len(item) + 1
        res.append(rack)
        space = [' ' for _ in range(maxWidth)]
        def _write_line(rack):
            word_num = len(rack)
            l = 0
            if word_num == 1:
                line = rack
                line.extend(space)
                return ''.join(line)[:maxWidth]
            for item in rack:
                l += len(item)
            base = (maxWidth-l) // (word_num-1)
            offset = (maxWidth-l) % (word_num-1)
            line = []
            space_1 = ' ' * (base+1)
            space_2 = ' ' * (base)
            for i in range(len(rack)-1):
                line.append(rack[i])
                if offset > 0:
                    line.append(space_1)
                    offset -= 1
                else:
                    line.append(space_2)
            line.append(rack[-1])
            return ''.join(line)
        def _write_last(rack):
            line = []
            l = 0
            for i in range(len(rack)):
                line.append(rack[i])
                line.append(' ')
            line.extend(space)
            return ''.join(line)[:maxWidth]




        for i in range(len(res)-1):
            res[i] = _write_line(res[i])
        res[-1] = _write_last(res[-1])

        return res
