'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Have you met this question in a real interview? Yes
Example
Given encoded message 12, it could be decoded as AB (1 2) or L (12).
The number of ways decoding 12 is 2.
'''
class Solution:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        if not s:
            return 0
        DP = [1 for i in xrange(len(s)+1)]
        for i in xrange(2,len(s)+1):
            if s[i-1] == '0':
                if 0 < int(s[i-2:i]) <= 26:
                    DP[i] = DP[i-2]
                else:
                    return 0
            elif int(s[i-2:i]) <= 26:
                DP[i] = DP[i-1] + DP[i-2]
            else:
                DP[i] = DP[i-1]
        return DP[len(s)]
    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]