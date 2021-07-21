'''
Given a string source and a string target, find the minimum window in source which will contain all the characters in target.

 Notice

If there is no such window in source that covers all characters in target, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in source.

Have you met this question in a real interview? Yes
Clarification
Should the characters in minimum window has the same order in target?

Not necessary.
Example
For source = "ADOBECODEBANC", target = "ABC", the minimum window is "BANC"
'''
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        table = {}
        minLen = float('inf')
        for char in target:
            table.setdefault(char,0)
            table[char] += 1
        targetLen = len(target)
        left = 0
        resHead = 0
        for i in xrange(len(source)):
            if source[i] in table:
                table[source[i]] -= 1
                if table[source[i]] > 0:
                    targetLen -= 1
            while targetLen ==0 :
                if minLen > i - left:
                    resHead = left
                    minLen = i - left
                if source[left] in table and table[source[left]] == 0:
                    table[source[left]] += 1
                    targetLen += 1
                left += 1
        if targetLen == float('inf'):
            return ''
        else:
            end = resHead+minLen
            return source[resHead:end]
def main():
    test1 = "ADOBECODEBANC"
    test2 = "ABC"
    sol = Solution()
    sol.minWindow(test1,test2)
if __name__ == '__main__':
    main()