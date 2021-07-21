'''
Requirement Check
'''
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        res = []
        res.append(S[0])
        cnt = 1
        for idx in range(1, len(S)):
            if S[idx] != S[idx-1]:
                res.append(str(cnt))
                res.append(S[idx])
                cnt = 1
            else:
                cnt +=1
        res.append(str(cnt))
        if len(res) < len(S): # Empty
            return ''.join(res)
        else:
            return S


