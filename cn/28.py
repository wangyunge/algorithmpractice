class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        window = len(needle)
        for idx in range(len(haystack) - window + 1):
            if haystack[idx:idx+window] == needle:
                return idx
        return -1
