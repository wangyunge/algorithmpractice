'''
Write a program to find the node at which the intersection of two singly linked lists begins.

 Notice

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Have you met this question in a real interview? Yes
Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        index = headA
        lengthA = 0
        while index:
            lengthA +=1
            index = index.next
        index = headB
        lengthB = 0
        while index:
            lengthB += 1
            index = index.next
        shortH = headA if lengthA < lengthB else headB
        longH = headA if lengthB < lengthA else headB

        diff = abs(lengthA - lengthB)
        count = 0
        while shortH and longH:
            if shortH == longH:
                return shortH 
            count +=1
            if count > diff:
                shortH = shortH.next
            longH = longH.next
