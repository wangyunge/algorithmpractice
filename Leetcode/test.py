class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        aux = [0] * (N + 1)
        for ci in citations:
            if ci >= N:
                aux[-1] += 1
            else:
                aux[ci] += 1
        cul = 0
        for i in range(N+1)[::-1]:
            cul += aux[i]
            if cul >= i:
                return i


def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    nums = [2,0,6,1,5]

    ret = Solution().hIndex(nums)

    out = intToString(ret)

    print out

if __name__ == '__main__':
    main()    

