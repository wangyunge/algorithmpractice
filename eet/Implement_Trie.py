'''
Implement a trie with insert, search, and startsWith methods.

'''
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.character = None
        self.val = None

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currNode = self.root
        for character in word:
            if character in currNode.children:
                currNode = currNode.children[character]
            else:
                return False
        if currNode.val == word:
            return True 
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: strxx
        :rtype: bool
        """
        currNode = self.root
        for character in prefix:
            if character in currNode.children:
                currNode = currNode.children[character]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")