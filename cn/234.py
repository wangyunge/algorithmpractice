# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next 
        cnt = 0
        cur = head 
        L = len(stack)
        while cnt < L // 2:
            if stack.pop() != cur.val:
                return False 
            cur = cur.next 
            cnt += 1
        return True 


             
