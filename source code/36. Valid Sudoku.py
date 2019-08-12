class Solution:
    def check_col(self,board, col):
        used = []
        for i in range(0, 9):
            if board[col][i] is not '.':
                if board[col][i] not in used:
                    used.append(board[col][i])
                else:
                    return False
        return True

    def check_row(self, board, row):
        used = []
        for i in range(0, 9):
            if board[i][row] is not '.':
                if board[i][row] not in used:
                    used.append(board[i][row])
                else:
                    return False
        return True

    def check_box(self, board, top_left_index):
        col = top_left_index[0]
        row = top_left_index[1]
        used = []
        for i in range(col, col + 3):
            for j in range(row, row + 3):
                # print(board[i][j], end=' ')
                if board[i][j] is not '.':
                    if board[i][j] not in used:
                        used.append(board[i][j])
                    else:
                        return False
            # print()
        return True

    def isValidSudoku(self, board):
        for cr in range(0, 9):
            if not self.check_col(board, cr):
                return False
            if not self.check_row(board, cr):
                return False
        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                if not self.check_box(board, (col, row)):
                    return False
        # self.check_box(board, (3, 3))
        return True



if __name__ == '__main__':
    sol = Solution()
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(sol.isValidSudoku(board))


