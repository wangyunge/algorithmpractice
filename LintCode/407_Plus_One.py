'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Have you met this question in a real interview? Yes
Example
Given [1,2,3] which represents 123, return [1,2,4].

Given [9,9,9] which represents 999, return [1,0,0,0].

'''
class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        digits.reverse()
        carry = 0
        for i in xrange(len(digits)):
            if i == 0:
                newD = (digits[i]+1)
            else:
                newD = digits[i] + carry
            digits[i] = newD%10
            carry = newD/10
        if carry == 1:
            digits.append(1)
        digits.reverse()
        return digits
def main():
    test = [9,9,9]
    sol = Solution()
    sol.plusOne(test)
if __name__ == '__main__':
    main()