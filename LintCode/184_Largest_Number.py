'''
Given a list of non negative integers, arrange them such that they form the largest number.

 Notice

The result may be very large, so you need to return a string instead of an integer.

Have you met this question in a real interview? Yes
Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.

'''
class Solution: 
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        if not num:
            return ''
        notZero = filter(lambda x: x != 0,num)
        if not notZero:
            return '0'
        for i in xrange(len(num)):
            for j in xrange(i,len(num)):
                if self.smaller(num[i],num[j]):
                    num[i],num[j] = num[j],num[i]
        num = map(lambda x: str(x),num)
        return ''.join(num)

    def smaller(self,a,b):
        strA = str(a)
        strB = str(b)
        i = 0
        while i < len(strA) and i < len(strB):
            if int(strA[i]) < int(strB[i]):
                return True
            elif int(strA[i]) > int(strB[i]):
                return False
            i += 1
        if len(strA) <= len(strB):
            return True
        else:
            return False 
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'