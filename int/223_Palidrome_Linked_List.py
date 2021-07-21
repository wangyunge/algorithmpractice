'''
Implement a function to check if a linked list is a palindrome.

Have you met this question in a real interview? Yes
Example
Given 1->2->1, return true
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        if not head:
            return True
        length = 0
        count = head
        while count:
            length += 1
            count = count.next
        mid = length/2
        step = 0
        left = None
        right = head
        while step < mid:
            step += 1
            tmp = right
            right = right.next
            tmp.next = left
            left = tmp
        if length%2 == 1:
            right = right.next
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True