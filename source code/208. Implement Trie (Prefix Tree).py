class Trie:
    def __init__(self):
        self.sons = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            # breakpoint()
            self.sons['#'] = None
            return
        if word[0] not in self.sons:
            self.sons[word[0]] = Trie()
        self.sons[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            if '#' in self.sons:
                return True
            else:
                return False
        if word[0] in self.sons:
            return self.sons[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        if prefix[0] in self.sons:
            return self.sons[prefix[0]].startsWith(prefix[1:])
        else:
            return False

if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'))
    print(obj.search('app'))
    print(obj.startsWith('app'))
    obj.insert('app')
    print(obj.search('app'))
