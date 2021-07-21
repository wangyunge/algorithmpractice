"""
搜索的时候考虑搜不到，搜到的结果在最左边，最右边
"""


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.table:
            self.table[key][1].append(timestamp)
            self.table[key][0].append(value)
        else:
            self.table[key] = [[value], [timestamp]]


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        def _bi_search(target, arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        if key in self.table:
            pos = _bi_search(timestamp, self.table[key][1])
            if pos != -1:
                return self.table[key][0][pos]
        return ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
