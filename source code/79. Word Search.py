class Solution:
    def search(self, board, x, y, sub_word, used):
        if len(sub_word) == 0:
            return True
        if sub_word[0] != board[x][y]:
            return False
        if len(sub_word) == 1:
            return True
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # print(board[x][y])
        for (i, j) in dir:
            if 0 <= x + i < len(board) and 0 <= y + j < len(board[x + i]) and (x + i, y + j) not in used:
                if self.search(board, x + i, y + j, sub_word[1:], used + [(x+i, y+j)]):
                    return True
        return False

    def exist(self, board, word):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if self.search(board, i, j, word, [(i, j)]):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    board =[
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = 'EECC'
    print(sol.exist(board, word))
