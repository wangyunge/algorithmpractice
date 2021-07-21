class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        B = nums[:]
        for i in range(1, len(nums)):
            B[i] = nums[i] + B[i-1]
        avg = B[-1] / m
        B.append(0)
        prev = -1
        for i in range(0, len(nums)):
            if B[i] - B[prev] > avg:
                if B[i] - B[prev] - avg < avg - (B[i-1] - B[prev]):
                    res = max(B[i]-B[prev], res)
                    prev = i
                else:
                    res = max(B[i-1]-B[prev])
                    prev = i-1
                    if B[i] - B[prev] > avg:
                        res = max(B[i]-B[prev], res)
                        prev = i
        res = max(B[i]-B[prev])


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[10**18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))

        return f[n][m]


