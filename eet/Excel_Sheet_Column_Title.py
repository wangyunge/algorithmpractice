'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        scale = 0
        while n > 0:
            res += self.toChar((n-1)%26)
            n = (n-1)/26
        return res[::-1]
    def toChar(self,n):
        return chr(ord("A")+n)
def main():
    sol = Solution()
    test = 52
    res = sol.convertToTitle(test)
    print res
if __name__ == '__main__':
    main()