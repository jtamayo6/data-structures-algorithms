class TrieNode:
    def __init__(self, isWord=False):
        self.children = [None]*26
        self.isWord = isWord

    def charToIndex(self, c):
        return ord(c) - ord('a')

    def insert(self, key):
        i = self.charToIndex(key[0])
        if len(key) == 1 and self.children[i] is None:
            self.children[i] = TrieNode(True)
        else:
            if self.children[i] is None:
                self.children[i] = TrieNode(False)
            self.children[i].insert(key[1:])

    def search(self, key):
        i = self.charToIndex(key[0])
        if self.children[i] is None:
            return False
        elif len(key) == 1:
            return self.children[i].isWord
        else:
            return self.children[i].search(key[1:])

class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def insert(self, key):
        self.root.insert(key)

    def search(self, key):
        return self.root.search(key)


if __name__ == "__main__":
    myTrie = Trie()
    myTrie.insert('car')
    myTrie.insert('cut')
    myTrie.insert('run')
    print(myTrie.search('cut'))
    print(myTrie.search('can'))