'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or headB:
            return -1
        lengthOfA = lengthOfB = 0
        h1 = headA
        while h1:
            lengthOfA += 1
            h1 = h1.next
        h2 = headB
        while h2:
            lengthOfB += 1
            h2 = h2.next
        h1 = headA if lengthOfA > lengthOfB else headB
        h2 = headB if h1 == headA else headA
        diff = abs(lengthOfA - lengthOfB)
        itera = 0
        while h1 and h2:
            if h1 == h2:
                return h1
            itera += 1
            if itera > diff:
                h2 = h2.next
            h1 = h1.next
        return -1
