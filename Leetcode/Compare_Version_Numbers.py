'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        res = 0
        version1 = version1.split(".")
        version2 = version2.split(".")
        while version1 and int(version1[-1]) == 0:
            del version1[-1]
        while version2 and int(version2[-1]) == 0:
            del version2[-1]
        itera = min(len(version1),len(version2))
        for i in xrange(itera):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
        if itera > 0 and i == itera-1:
            if len(version1) == len(version2):
                res = 0
            else:
                res = 1 if len(version1) > len(version2) else -1
        else:
            if len(version1) == len(version2):
                res = 0
            else:
                res = 1 if len(version1) > len(version2) else -1
        return res