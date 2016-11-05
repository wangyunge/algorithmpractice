'''
Given a string, find the length of the longest substring without repeating characters.

Have you met this question in a real interview? Yes
Example
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        import re
        s = re.sub(r'[^a-z]','',s)
        s = s.lower()
        if len(s) ==1 or len(s) ==1:
            return len(s)
        L = 0
        R = 0
        res = 0
        table = {}
        while R < len(s):
            if s[R] not in table or table[s[R]]+1 < L:
                table[s[R]] = R
                R += 1
            else:
                L = table[s[R]]+1
                table[s[R]] = R
                R += 1
            res = max(res,R-L)
        return res
def main():
    test = "gehmbfqmozbpripibusbezagafqtypz"
    sol = Solution()
    res = sol.lengthOfLongestSubstring(test) 
if __name__ == '__main__':
    main()

'''
1.the change of left index mush make the new length shorter,which means that table can only contains the characters in the interval between Left index and right index.

2.Write down the rule you want to follow not the methods. Methods are just the way you follow the rule.

3.Only contains letters, re.sub(r'[^a-zA-Z]','',s)


'''