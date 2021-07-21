'''
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

Have you met this question in a real interview? Yes
Example
Given -21->10->4->5, tail connects to node index 1，return 10

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
    @param head: The first node of the linked list.
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
    	if not head:
    		return head
    	helper = ListNode(0,head)

    	fast = helper
    	slow = helper
    	x = 1
    	fast = fast.next.next
    	slow = slow.next
    	while slow != fast:
    		x+=1
    		if not fast or not fast.next:
    			return null
    		fast = fast.next.next
    		slow = slow.next
    	circleLen = 1
    	slow = slow.next
    	while slow != fast:
    		slow = slow.next
    		circleLen += 1
    	k = x/circleLen
    	res = (k-1)*circleLen
    	while res > 0:
    		res -=1
    		head = head.next
    	return head