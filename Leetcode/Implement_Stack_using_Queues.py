"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_a = Queue.Queue()
        self.queue_b = Queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue_a.put(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.queue_a.qsize() > 1:
            self.queue_b.put(self.queue_a.get())
        res = self.queue_a.get()
        self.queue_a, self.queue_b = self.queue_b, self.queue_a
        return res

        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.queue_a.qsize() > 1:
            self.queue_b.put(self.queue_a.get())
        res = self.queue_a.get()
        self.queue_b.put(res)
        self.queue_a, self.queue_b = self.queue_b, self.queue_a
        return res
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue_a.empty()  


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()