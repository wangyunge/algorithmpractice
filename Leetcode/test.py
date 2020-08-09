from math import floor
import copy
class Solution:
    def minEatingSpeed(self, piles, H) :
        self.H = H
        self.piles = piles
        left = 0 
        right = max(piles)
        while left < right:
            mid = floor((left + right)/2) 
            if self._eat(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if self._eat(left) else left + 1

    def _eat(self, k):
        h = 0
        plate = 0
        deep_piles = copy.deepcopy(self.piles)
        while deep_piles or plate > 0:
            if plate == 0:
                plate = deep_piles.pop()
            plate = max(0, plate - k)
            h += 1
        return self.H >= h


def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    nums = [70]

    ret = Solution().minEatingSpeed(nums, 312884469)

    out = intToString(ret)

    print(out)

if __name__ == '__main__':
    main()    

