class TrieNode:
    def __init__(self, ch):
        self.wordset = set()
        self.ch = ch
        self.sublist = None

    def add_sublist(self):
        self.sublist = [TrieNode(-1) for _ in range(26)]

    def set_val(self, ch):
        self.ch = ch


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(-1)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for ch in word:
            k = ord(ch) - 97
            if not p.sublist:
                p.add_sublist()
            p.sublist[k].set_val(ch)
            p = p.sublist[k]
        p.wordset.add(word)

    def search_word(self, word: str):
        p = self.root
        for ch in word:
            k = ord(ch) - 97
            if not p or not p.sublist or p.sublist[k].ch == -1:
                return None
            p = p.sublist[k]
        return p

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.search_word(word)
        if not p:
            return False
        else:
            return True if word in p.wordset else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.search_word(prefix)
        return True if p else False


# Your Trie object will be instantiated and called as such:
word = "app"
prefix = "apps"
obj = Trie()

app = "app"
apple="apple"
beer="beer"
add="add"
jam="jam"
rental="rental"

apps="apps"

obj.insert(app)
obj.insert(apple)
obj.insert(beer)
obj.insert(add)
obj.insert(jam)
obj.insert(rental)



# print(obj.search(word))
# print(obj.search(prefix))
# print(obj.startsWith(prefix))
# obj.insert(prefix)
# print(obj.search(prefix))
print(obj.startsWith(apps))
