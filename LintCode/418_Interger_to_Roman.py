'''
Given an integer, convert it to a roman numeral.

The number is guaranteed to be within the range from 1 to 3999.

Have you met this question in a real interview? Yes
Clarification
What is Roman Numeral?

https://en.wikipedia.org/wiki/Roman_numerals
https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97
http://baike.baidu.com/view/42061.htm
Example
4 -> IV

12 -> XII

21 -> XXI

99 -> XCIX

more examples at: http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
'''
class Solution:
    # @param {int} n The integer
    # @return {string} Roman representation
    def intToRoman(self, n):
    	n = str(n)
    	n = n[::-1]
        res = ''
        for i in xrange(len(n)):
        	tmp = self.convert(n[i],i)
        	res = tmp + res
       	return res
    def convert(self,number,index):    	
        ones = ['I','X','C','M']
        fives = ['V','L','D']
        one = ones[index]
        five = fives[index]
        ten = ones[index+1]
        if number == '0':
        	return ''
    	if number == '1':
    		return	ones[index]
    	if number == '2':
    		return one + one
    	if number == '3':
    		return one + one + one
    	if number == '4':
    		return one + five
    	if number == '5':
    		return five
    	if number == '6':
    		return five + one
    	if number == '7':
    		return five + one + one
    	if number == '8':
    		return five + one + one + one
    	if number == '9':
    		return one + ten
