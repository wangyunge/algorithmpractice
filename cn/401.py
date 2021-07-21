'''
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。

例如，下面的二进制手表读取 "3:25" 。


给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。

小时不会以零开头：

例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
分钟必须由两位数组成，可能会以零开头：

例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
 

示例 1：

输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
示例 2：

输入：turnedOn = 9
输出：[]

'''


class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        def _hour_dfs(base, left, cumulate):
            if left == 0 :
                hours.append(cumulate) 
            elif base <= 8:
                _hour_dfs(base*2, left, cumulate)
                if left > 0:
                    cumulate += base
                    if cumulate <= 11:
                        _hour_dfs(base*2, left-1, cumulate)
        def _minute_dfs(base, left, cumulate):
            if left == 0:
                minutes.append(cumulate)
            elif base <= 32:
                _minute_dfs(base*2, left, cumulate)
                if  left > 0:
                    cumulate += base
                    if cumulate < 60:
                        _minute_dfs(base*2, left-1, cumulate)
        def _str_num(x):
            if x < 10:
                return '0'+str(x)
            else:
                return str(x)
        res = []
        for i in range(0, turnedOn+1):
            hours = []
            minutes = []
            _hour_dfs(1, i, 0)
            _minute_dfs(1, turnedOn-i, 0)
            for hour in hours:
                for minute in minutes:
                    res.append(str(hour)+':'+_str_num(minute))
        return res 

