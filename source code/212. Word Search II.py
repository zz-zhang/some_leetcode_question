class Solution:
    def loc_legal(self, board, x, y):
        if x < 0 or x >= len(board):
            return False
        if y < 0 or y >= len(board[0]):
            return False
        return True

    def reachable(self, board, x, y, word, block):
        if len(word) == 0:
            return True
        dir = [(-1, 0),
               (1, 0),
               (0, -1),
               (0, 1)]
        for d in dir:
            if self.loc_legal(board, x + d[0], y + d[1]) and board[x + d[0]][y + d[1]] == word[0] and (x + d[0], y + d[1]) not in block:
                if self.reachable(board, x + d[0], y + d[1], word[1:], block + [(x + d[0], y + d[1])]):
                    return True
        return False

    def findWords(self, board, words):
        res = []
        for word in words:
            found = False
            for x in range(len(board)):
                for y in range(len(board[0])):
                    if board[x][y] == word[0] and self.reachable(board, x, y, word[1:], [(x, y)]):
                        res.append(word)
                        found = True
                        break
                if found:
                    break
        return res

if __name__ == '__main__':
    sol = Solution()
    board = [
      ["a", "a"]
    ]
    words = ["aaa"]
    print(sol.findWords(board, words))
