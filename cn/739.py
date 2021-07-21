class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0 for _ in T]
        for i, this_t in enumerate(T):
            while stack and T[stack[-1]] < this_t:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

