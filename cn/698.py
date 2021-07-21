class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        self.res = False
        target = sum(nums) / k
        if sum(nums) % k > 1:
            return False
        def _dfs(g, tmp):
            if g == 0:
                self.res = True
            else:
                for i, num in enumerate(nums):
                    if num == 0.5 :
                        continue
                    if tmp + num < target:
                        save = nums[i]
                        nums[i] = 0.5
                        _dfs(g, tmp+num)
                        nums[i] = save
                    elif tmp + num == target:
                        save = num[i]
                        num[i] = 0.5
                        _dfs(g-1, tmp+num)
                        nums[i] = save
                        if self.res :
                            break
        _dfs(k, 0)
        return self.res

# ！！！被自己忽略的一个关键信息：
# 把数组分为k个相等部分，那么每一部分的和就等于sum(nums)/k
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        partial_sum, mod = divmod(sum(nums), k)
        # 不能整除，肯定不行
        if mod != 0:
            return False

        def dfs(groups) -> bool:
            if not nums:
                return True
            # 优化，接排序
            # 数组被排序过，pop()得到的数为此时最大
            num = nums.pop()
            for i in range(k):
                groups[i] += num
                if groups[i] <= partial_sum:
                    if dfs(groups):
                        return True
                groups[i] -= num
                # 优化
                # 当前项复原后为0，那么后面的结果和此时结果相同
                # 既然当前项都不行，那么之后也不用继续搜索
                if groups[i] == 0:
                    break
            # 复原数组
            nums.append(num)
            return False

        # 优化
        # 排序后先尝试大的数，缩小搜索空间
        nums.sort()
        # 优化
        # 最后一项大于partial_sum，直接返回False
        if nums[-1] > partial_sum:
            return False
        # 优化
        # 缩小搜索空间
        while nums and nums[-1] == partial_sum:
            nums.pop()
            k -= 1
        return dfs([0] * k)
