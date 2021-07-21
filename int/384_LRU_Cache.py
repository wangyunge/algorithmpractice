'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Have you met this question in a real interview? Yes
'''
class Node:
    def __init__(self,prev,val):
        self.val = val
        self.prev = prev
        self.next = None
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.table = {}
        self.head = Node(None,0)
        self.tail = self.head
        self.capacity = capacity
        self.usage = 0

    # @return an integer
    def get(self, key):
        if key in self.table:
            setNode = self.table[key]
            if setNode == self.tail:
                self.tail = setNode.prev
            #delete
            setNode.prev.next = setNode.next
            setNode.next.prev = setNode.prev
            #insert
            self.head.next.prev= setNode
            setNode.next = self.head.next
            self.head.next = setNode
            setNode.prev = self.head

            return setNode.val[1]
        else:
            return -1
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        getExit = self.get(key)
        if getExit == -1:
            #new node and new key
            setNode = Node(self.head,(key,value))
            self.table[key] = setNode
            #insert
            self.head.next.prev = setNode
            setNode.next = self.head.next
            self.head.next = setNode
            self.usage += 1
            if self.usage == 0:
                setNode = Node(self.head,(key,value))
                self.tail = setNode
            elif self.usage >= self.capacity:
                #del tail
                delKey = self.tail.val[0]
                del self.table[delKey]
                self.tail = self.tail.prev
                self.tail.next = None
        elif getExit != value:
            self.table[key].val[1] = value




