'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
from queue import Queue
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        visited = set()
        not_visited = set(wordList)
        queue = Queue()
        queue.put((beginWord,1))
        while not queue.empty():
            (node,length) = queue.get()
            if self.isAdjacent(node,endWord):
                return length + 1
            for word in list(not_visited):
                if word not in visited and self.isAdjacent(node,word):
                    queue.put((word,length+1))
                    visited.add(word)
                    not_visited.remove(word)
        return 0
    def isAdjacent(self,wordA,wordB):
        num = 0
        for i in range(0,len(wordA)):
            if wordA[i] != wordB[i]:
                num+=1
        return num == 1

def main():
    test = set(["hot","dog","cog","pot","dot"])
    sol = Solution()
    res = sol.ladderLength("hot","dog",test)
if __name__ == '__main__':
    main()

'''
Notes:
1. BFS for shortest path
2. HashTable to prevent circle
3. Build the adjacents table with wildcard. 
4. Bidirectional Search.
'''