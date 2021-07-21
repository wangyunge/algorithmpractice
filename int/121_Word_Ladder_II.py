'''
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
 Notice

All words have the same length.
All words contain only lowercase alphabetic characters.
Have you met this question in a real interview? Yes
Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
'''
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        from Queue import Queue
        queue = Queue()
        res = []
        queue.put((start,[start],set([])))
        maxLength = len(dict)
        while not queue.empty():
            (word,path,pathSet) = queue.get()
            if len(path) > maxLength:
                break
            if self.adjcent(word,end):
                res.append(path+[end])
                maxLength = len(path)
            for step in dict:
                if self.adjcent(word,step) and step not in pathSet:
                    queue.put((step,path+[step],pathSet.add(step)))

        return res
    def adjcent(self,A,B):
        count = 0
        for i in xrange(len(A)):
            if A[i] != B[i]:
                count += 1
            if count ==2:
                break
        return count == 1