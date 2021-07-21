class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def _dfs(arr):
            end = len(arr) - 1
            for i in range(len(arr)):
                tmp = arr[i]
                for j in range(i+1, len(arr)):
                    ops = arr[i]+arr[j]
                    arr[i] = ops
                    arr[end], arr[j] = arr[j], arr[end]
                    _dfs(arr[:end])

                    arr[end], arr[j] = arr[j], arr[end]
                    ops = arr[i]-arr[j]
                    arr[i] = ops
                    arr[end], arr[j] = arr[j], arr[end]
                    _dfs(arr[:end])

                    arr[end], arr[j] = arr[j], arr[end]
                    ops = arr[i]*arr[j]
                    arr[i] = ops
                    arr[end], arr[j] = arr[j], arr[end]
                    _dfs(arr[:end])

                    arr[end], arr[j] = arr[j], arr[end]
                    if arr[i] != 0
                        ops = arr[j]/arr[i]
                        arr[i] = ops
                        arr[end], arr[j] = arr[j], arr[end]
                        _dfs(arr[:end])
                        arr[end], arr[j] = arr[j], arr[end]

                    if arr[j] != 0
                        ops = arr[i]/arr[j]
                        arr[i] = ops
                        arr[end], arr[j] = arr[j], arr[end]
                        _dfs(arr[:end])
                        arr[end], arr[j] = arr[j], arr[end]
                arr[i] = tmp
