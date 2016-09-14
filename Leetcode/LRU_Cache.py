'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

'''
class LRUCache(object):
    class Node(object):
        def __init__(self,val,prev,next):
            self.val = val
            self.prev = prev
            self.next = None
    class DLList(object):
        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        tableOfVal = {}
        tableOfCount = {}
        self.capacity = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        tableOfCount[key] = tableOfCount[key] + 1
        return tableOfVal[key]
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if len(table) <= self.capacity:
            tableOfCount[key] = 0
            tableOfVal[key] = 