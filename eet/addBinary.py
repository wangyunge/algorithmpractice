class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        res=''
        acc = 0
        if len(a)<len(b):
            a,b = b,a
        L = len(a)
        S = len(b)
        for i in xrange(1,L+1):
            if i <= S:
                add = int(a[-i])+int(b[-i])+acc
                if add==0:
                    res+='0'
                    acc=0
                elif add==1:
                    res+='1'
                    acc=0
                elif add==2:
                    res+='0'
                    acc=1
                elif add==3:
                    res+='1'
                    acc=1
                else:
                    return False
            else:
                add = int(a[-i])+acc
                if add==0:
                    res+='0'
                    acc=0
                elif add==1:
                    res+='1'
                    acc=0
                elif add==2:
                    res+='0'
                    acc=1
                elif add==3:
                    res+='1'
                    acc=1
                else:
                    return False
        if acc==1:
            res+='1'
        return res[::-1]
def main():
    a='1001'
    b='11'
    sol = Solution()
    print sol.addBinary(a,b)

if __name__ == '__main__':
    main()