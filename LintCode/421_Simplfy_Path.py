'''
Given an absolute path for a file (Unix-style), simplify it.

Have you met this question in a real interview? Yes
Example
"/home/", => "/home"

"/a/./b/../../c/", => "/c"

Did you consider the case where path = "/../"?

In this case, you should return "/".

Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".

In this case, you should ignore redundant slashes and return "/home/foo".
'''
class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        pathList = path.split("/")
        stack =[]
        for directory in pathList:
            if not directory:
                continue
            elif directory == '.':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(directory)
        path = '/'.join(stack)
        return '/'+path