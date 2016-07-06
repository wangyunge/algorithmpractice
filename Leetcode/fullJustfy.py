# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.

# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.

# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.

# click to show corner cases.

# Subscribe to see which companies asked this question

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res =[]
        i=0
        LineHead = 0
        L=0
        R=0
        while i <= len(words):
            if L + len(words(i)) < maxWidth:
                R+=1
                L = L + len(words[i]) +1 
                i+=1
            else:
                i-=1
                spaces = maxWidth - L + (i - LineHead + 1)
                if i - LineHead==0:
                    spaces = maxWidth-L
                    headSpace = 0
                space = spaces/(i -LineHead)
                headSpace = spaces%(i -LineHead)
                line = ''
                j=0
                for indexInline in xrange(LineHead,i+1):
                    if j<headSpace:
                        line+=words[indexInline] + ' '*space + 1
                    else:
                        line+=words[indexInline] + ' '*space
                    j+=1
                i+=1
                LineHead = i
                res+=line
        return res
def main():

if __name__ == '__main__':
    main()