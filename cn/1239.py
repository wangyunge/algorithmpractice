class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        bit_arr = []
        base = ord('a')
        for word in arr:
            word_code = set()
            valid = True
            for char in word:
                code = ord(char) - base
                if code in word_code:
                    valid = False
                    break
                else:
                    word_code.add(code)
            if valid:
                res.append(word_code)



        bit_map = [0 for _ in range(26)]

        def _set(word):

        def _rest(word):

