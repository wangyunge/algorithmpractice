# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        helper = ListNode(0)
        head = helper
        digit=1
        plus=0
        while l1 or l2:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            levelRes = (a+b+plus)%10
            plus = (a+b+plus)/10
            
            head.next = ListNode(levelRes)
            head = head.next
        if plus==1:
            head.next = ListNode(1)
        return helper.next
