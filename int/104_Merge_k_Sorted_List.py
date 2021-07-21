'''
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Have you met this question in a real interview? Yes
Example
Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
        tmp = []
        for node in lists:
            if node:
                tmp.append(node)
        lists = tmp 
        helper = ListNode(0,None)
        index = helper
        while len(lists)>1:
            self.bubble(lists)
            luckOne = lists.pop()
            index.next = luckOne
            if luckOne.next:
                lists.append(luckOne.next)
            index = index.next
        index.next = lists[0] if lists else None 
        return helper.next
    def bubble(self,lists):
        for i in xrange(len(lists)-1):
            if lists[i].val < lists[i+1].val:
                lists[i],lists[i+1] = lists[i+1],lists[i]

    def mergeKLists(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next
        return dummy.next