class WordDictionary:

    class Node:
        def __init__(self, char):
            self.val = char
            self.leaves = {}
            # self.leaves_val = set()

    def __init__(self):
        self.root = self.Node('')
        

    def addWord(self, word: str) -> None:
        word = word + '|'
        node = self.root
        for char in word:
            if char not in node.leaves:
                new_node = self.Node(char)
                node.leaves[char] = new_node
                node = new_node
            else:
                node = node.leaves[char]
        

    def search(self, word: str) -> bool:
        # print(self)
        word = word + '|'
        node = self.root
        q = [(node, 0)]

        while q:
            cur_node, word_idx = q.pop()
            if word_idx == len(word):
                return True
            char = word[word_idx]
            # breakpoint()

            if char == '.':
                if cur_node.leaves:
                    for next_char, next_node in cur_node.leaves.items():
                        q.append((next_node, word_idx + 1))
            else: 
                if char in cur_node.leaves:
                    q.append((cur_node.leaves[char], word_idx + 1))

        
        return False

    def __str__(self):
        node = self.root

        res = []
        sub_str = ''
        self._get_words(node, sub_str, res)
        return ','.join(res)
        
    def _get_words(self, node, sub_str, res):
        if node.val != '|':
            sub_str = sub_str + node.val
            # res.append(sub_str)        
            for next_char, next_node in node.leaves.items():
                self._get_words(next_node, sub_str, res)
        else:
            res.append(sub_str + '|')
            return
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')

# print(obj)
print(obj.search('an.'))

# obj.addWord('a')
# print(obj.search('a.'))