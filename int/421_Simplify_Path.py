'''
Given an absolute path for a file (Unix-style), simplify it.

Have you met this question in a real interview? Yes
Example
"/home/", => "/home"

"/a/./b/../../c/", => "/c"
'''
class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        