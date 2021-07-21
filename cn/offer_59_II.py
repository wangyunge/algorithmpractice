from collections import deque
class MaxQueue(object):

    def __init__(self):
        self.queue = deque()
        self.priority_queue = deque()


    def max_value(self):
        """
        :rtype: int
        """
        if self.priority_queue:
            return self.priority_queue[0]
        return -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)

        while self.priority_queue and self.priority_queue[-1] < value:
            self.priority_queue.pop()
        self.priority_queue.append(value)



    def pop_front(self):
        """
        :rtype: int
        """
        res = self.queue.popleft() if self.queue else None
        if self.priority_queue and res == self.priority_queue[0]:
            self.priority_queue.popleft()
        if res:
            return res
        else:
            return -1



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
