'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.character = None
        self.val = None
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        currNode = self.root
        for character in word:
            if character in currNode.children:
                currNode = currNode.children[character]
            else:
                currNode.children[character] = TrieNode() 
                currNode = currNode.children[character]
        currNode.val = word
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        found = False
        def DFS(currNode,leftchar):
            for i in xrange(len(leftchar)):
                if leftchar[i] == '.':
                    for node in currNode.children:
                        DFS(node,leftchar[i+1:])
                elif leftchar[i] in currNode.children:
                    currNode = currNode.children[leftchar[i]]
                else:
                    return False
            if currNode.val:
                found = True
            return False
        DFS(self.root,word)
        return found


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")