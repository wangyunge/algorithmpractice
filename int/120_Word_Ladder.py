'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
 Notice

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
Have you met this question in a real interview? Yes
Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
    	from Queue import Queue
    	queue = Queue()

    	queue.put((start,1))
    	while not queue.empty():
    		(word,depth) = queue.get()
    		tmp = []
    		if self.adjcent(word,end):
    			return depth+1
    		for step in dict:
    			if self.adjcent(word,step):
    				queue.put((step,depth+1))
    			else:
    				tmp.append(step)
    		dict = tmp
    	return 0

    def adjcent(self,A,B):
    	count = 0
    	for i in xrange(len(A)):
    		if A[i] != B[i]:
    			count += 1
    	return count == 1