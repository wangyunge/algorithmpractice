"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:

Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].


Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

"""

from heapq import *
class FreqStack(object):

    def __init__(self):
        self.heap = []
        self.table = {}


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        count = self.table.get(x, 0) + 1
        self.table[x] = count
        heappush(self.heap, (count, x))


    def pop(self):
        """
        :rtype: int
        """
        x, _ = heappop(self.heap)
        self.table[x] -= 1
        return x




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()



class FreqStack(object):

    def __init__(self):
        self.cnt2num = []
        self.num2cnt = {}
        self.top_cnt = 0



    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        count = self.num2cnt(x, 0) + 1
        self.num2cnt[x] = count
        if count > self.top_cnt:
            self.cnt2num.append([])
        self.cnt2num[count].append(x)


    def pop(self):
        """
        :rtype: int
        """
        """
        Notes: pop ops dones not delete the element. it just remove one apperance of this element. decrease the count
        while self.top_cnt > 0:
            while self.cnt2num[self.top_cnt]:
                res = self.cnt2num[self.top_cnt].pop()
                if self.num2cnt[res] > 0:
                    self.num2cnt[res] = 0
                    return res
                self.top_cnt -= 1

        return
        """



