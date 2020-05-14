#Implement a trie with insert, search, and startsWith methods.
#
#Example:
#
#Trie trie = new Trie();
#
#trie.insert("apple");
#trie.search("apple");   // returns true
#trie.search("app");     // returns false
#trie.startsWith("app"); // returns true
#trie.insert("app");   
#trie.search("app");     // returns true
#Note:
#
#You may assume that all inputs are consist of lowercase letters a-z.
#All inputs are guaranteed to be non-empty strings.


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}      # mapping from letter to child TrieNodes
        self.terminal = False   # flag indicates whole word

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        self.root.terminal = True   # empty string is a whole word

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:  # create a node if it does not exist
                node.children[c] = TrieNode()
            node = node.children[c]
        node.terminal = True            # set to True at end of word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.terminal            # only True if terminal

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True