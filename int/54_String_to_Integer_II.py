'''
Implement function atoi to convert a string to an integer.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Have you met this question in a real interview? Yes
Example
"10" => 10
"-1" => -1
"123123123123123" => 2147483647
"1.0" => 1
'''
class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        str.strip()
        # write your code here
        try:
            INT_MAX = 2147483647
            INT_MIN = -2147483648
            if '-' in str:
                sign = -1
                str = str[1:]
            else:
                sign = 1
            dotArray = str.split(".")

            beforeDot = dotArray[0]

            #before dot part
            resLarge = 0
            for i in xrange(len(beforeDot)):
                resLarge = resLarge*10 + int(beforeDot[i])
            res = resLarge*sign

            if res > INT_MAX:
                return INT_MAX
            elif res < INT_MIN:
                return INT_MIN
            else:
                return res
        except:
            return 0