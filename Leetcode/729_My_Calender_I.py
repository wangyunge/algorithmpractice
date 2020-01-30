'''
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
 

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
'''

class Node(object):
    def __init__(self, start, end):
        self.left = None 
        self.right = None 
        self.start = start 
        self.end = end
    def insert(self, new_node):

        if self.end <= new_node.start:
            if self.right == None:
                self.right = new_node
                return True 
            return self.right.insert(new_node)
        elif self.start >= new_node.end:
            if self.left == None:
                self.left = new_node    
                return True 
            return self.left.insert(new_node)
        else:
            return False

class MyCalendar(object):

    def __init__(self):
        self.root = None 

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start,end)
            return True
        else:
            return self.root.insert(Node(start, end))
    

'''
Note:
Type of Problem:
Area Intersection:
1. Check they contains overlap or not: De Morgan Rule. Becasue the intersection include too many conditons.
2. Binary Search Tree. O(log(n)) search and insert time complexity. 
3. Recursion require return the recursed function. G


'''