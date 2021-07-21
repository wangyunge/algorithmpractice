'''
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

 Notice

min operation will never be called if there is no number in the stack.
'''
class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []

    def push(self, number):
        # write yout code here
        if self.stack:
            lastMin = self.stack[-1][1]
            self.stack.append((number,min(number,lastMin)))
        else:
            self.stack.append((number,number))
    def pop(self):
        # pop and return the top item in stack
        item = self.stack.pop()
        return item[0]

    def min(self):
        # return the minimum number in stack
        if self.stack:
            return self.stack[-1][1]
        else:
            return 0
