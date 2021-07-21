'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

'''
class LRUCache(object):
    class Node(object):
        def __init__(self,val):
            self.val = val
            self.key = key
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(None, None)
        self.tail = self.head
        self.table = {}
        self.capacity = capacity


    def get(self, key):
        """
        :rtype: int
        """
        if key in self.table:
            node = self.table[key]
            node.prev.next, node.next.prev = node.next, node.prev
            self.head.prev = node
            node.next = self.head
            self.head = node
            return node.val
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.table:
            _ = self.get(key)
        else:
            node = Node(value, key)
            self.head.prev = node
            node.next = self.head
            self.head = node
            if len(table) > self.capacity:
                del self.table[self.tail.key]
                self.tail = self.tail.prev


