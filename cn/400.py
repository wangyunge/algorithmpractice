class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 Generate
        # 2 Locate
        # 1-9 1 9 * 1 = 9
        # 10-99 90 * 2 = 180
        # 100-999 900 * 3 = 2700
        ladder = 0
        digit_num = 0
        tens = 0.1
        while ladder < n:
            tens *= 10
            digit_num += 1
            interval = 9 * tens * digit_num
            ladder += interval
        ladder -= interval
        offset = n - ladder
        num = offset // digit_num + tens
        pos = offset % digtt_num
        return str(num)[]



