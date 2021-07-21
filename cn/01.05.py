'''
del , replace, insert
'''
class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        if first == second:
            return True
        f = len(first)
        s = len(second)
        if f < s:
            first, second = second, first
        d = False
        r = False
        i = 0
        while i < min(f, s):
            if first[i] == second[i]:
               i +=1 
            else:
                break
        d = False if f==s else first[i+1:] == second[i:]
        r = False if f != s else first[i+1:] == second[i+1:]
        return d or r


'''
exit the loop and start from the end point , trigger is in the loop
add the trigger out the loop
'''