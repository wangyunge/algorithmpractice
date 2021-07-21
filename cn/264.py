"""
n the
2, 3 , 5
"""

import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        heap = [2, 3, 5]
        idx = 1
        num = 1
        visted = set()
        while idx < n:
            num = heapq.heappop(heap)
            if num in visted:
                continue
            idx += 1
            visted.add(num)
            mul = [2*num, 3*num, 5*num]
            for item in mul:
                heapq.heappush(heap, item)
        return num
"""
方法一中的预计算操作较为繁琐，可以通过动态规划优化。

让我们从数组中只包含一个丑数数字 1 开始，使用三个指针 i_2i 
2
​   
 , i_3i 
3
​   
  和 i_5i 
5
​   
 ，标记所指向丑数要乘以的因子。

算法很简单：在 2 \times \textrm{nums}[i_2]2×nums[i 
2
​   
 ]，3 \times \textrm{nums}[i_3]3×nums[i 
3
​   
 ] 和 5 \times \textrm{nums}[i_5]5×nums[i 
5
​   
 ] 选出最小的丑数并添加到数组中。并将该丑数对应的因子指针往前走一步。重复该步骤直到计算完 1690 个丑数。

"""
















class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2: 
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
            
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]

