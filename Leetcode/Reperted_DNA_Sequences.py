'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        table = {}
        for i in xrange(len(s)-10):
            if s[i:i+10] not in table:
                table[s[i:i+10]] = (1,i+10)
            elif i >= table[s[i:i+10]][1]:
                table[s[i:i+10]] = (table[s[i:i+10]][1]+1,i+10)
        res = []
        for string,count in table.iteritems():
            if count[0] > 1:
                res.append(string)
        return res
def main():
    sol = Solution()
    test = "AAAAAAAAAAA" 
    res = sol.findRepeatedDnaSequences(test)
if __name__ == '__main__':
    main()