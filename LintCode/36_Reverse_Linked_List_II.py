'''
Reverse a linked list from position m to n.

 Notice

Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

Have you met this question in a real interview? Yes
Example
Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
'''
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        helper = ListNode(0,head)
        slow = helper
        fast = helper.next
        step = 0
        while fast:
            step +=1
            if step == m:
                start = slow
                start2 = fast
                slow = slow.next
                fast = fast.next
            elif step > m and step <= n:
                tmp = fast.next
                fast.next = slow
                slow = fast
                fast = tmp
            elif step <m:
                slow = slow.next
                fast = fast.next
            else:
                break
        start.next = slow
        start2.next = fast
        return helper.next