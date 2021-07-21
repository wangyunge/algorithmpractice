'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

Subscribe to see which companies asked this question

Show Tags
Show Similar Problems
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 1. m < l, n< l
        # 2.null input
        # 3. m=1
        # 4. n=L
        if not head:
            return head

        # Find the start
        # Find the end
        dummy = ListNode()
        dummy.next = head
        start = dummy
        idx = 1
        while idx < m and start:
            idx += 1
            start = start.next

        end = start
        while idx <= n+1 and end:
            idx +=1
            end = end.next

        # reverse start.next and end.prev
        prev = end
        cur = start.next
        while cur != end:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        start.next = prev

        return head





class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i=1
        if m!=1:
            curr =head
            while i<m-1:
                curr = curr.next
                i+=1
            breakPoint = curr
            breakHead = curr.next
            c1 = curr.next
            c2 = c1.next if c1 else None
            i+=1
        else:
            c1 = head
            c2 = c1.next if c1 else None
        while i < n:
            tmp = c2.next
            c2.next = c1
            c1 = c2
            c2 = tmp
            i+=1

        if m!=1:
            breakPoint.next = c1
            if breakHead.next:
                breakHead.next= c2
        else:
            head = c1
        return head




