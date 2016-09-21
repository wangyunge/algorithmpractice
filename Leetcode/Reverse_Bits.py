'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reversedBits = bin(n)[2:][::-1]
        resBits = ''
        for x in xrange(32):
            if x < len(reversedBits):
                resBits += reversedBits[x]
            else:
                resBits += '0'
        return int(resBits,2)
