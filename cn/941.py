"""
给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

arr.length >= 3
在 0 < i < arr.length - 1 条件下，存在 i 使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
 



 

示例 1：

输入：arr = [2,1]
输出：false
示例 2：

输入：arr = [3,5,5]
输出：false
示例 3：

输入：arr = [0,3,2,1]
输出：true
"""

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # slop
        slop = True
        # peak
        peak = False
        for idx in range(1, len(arr)):
            if not peak:
                if arr[idx] < arr[idx-1]:
                    peak = True
                elif arr[idx] == arr[idx-1]:
                    slop = False
                    break
            else:
                if arr[idx] >= arr[idx-1]:
                    slop = False
                    break
        return peak and slop


