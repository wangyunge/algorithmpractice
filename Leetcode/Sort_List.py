'''
Sort a linked list in O(n log n) time using constant space complexity.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        headList = []
        while head:
            headList.append(self.merge(head,head.next))
            if head.next:
                head = head.next.next
            else:
                break
        while len(headList)>1:
            tempList = []
            while i < len(headList)-1:
                tempList.append(self.merge(headList[i],headList[i+1]))
                i+=2
            headList = headList[i-1:] + tempList
        return  headList[0]
        
    def merge(self,h1,h2):
        if not h2:
            return h1
        helperHead = ListNode(0)
        index = helperHead
        while h1 and h2:
            if h1.val < h2.val:
                index.next = h1
                h1 = h1.next
            else:
                index.next = h2
                h2 = h2.next
            index = index.next
        index.next = h1 if h1 else h2
        return helperHead.next
