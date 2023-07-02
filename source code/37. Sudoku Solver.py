from pprint import pprint
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.avoid = {(i, j): set() for i in range(9) for j in range(9)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    for k in range(9):
                        self.avoid[(i, k)].add(board[i][j])
                        self.avoid[(k, j)].add(board[i][j])
                        start_r = (i // 3) * 3
                        start_c = (j // 3) * 3
                        for r in range(start_r, start_r + 3):
                            for c in range(start_c, start_c + 3):
                                self.avoid[(r, c)].add(board[i][j])

        pprint(self.avoid)
        self.dfs(board)
        
    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if num not in self.avoid[(i, j)] and self.is_valid(board, i, j, num):
                            board[i][j] = num
                            if self.dfs(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True
                        

    def is_valid(self, board, i, j, num):
        for k in range(9):
            if board[i][k] == num:
                return False
        for k in range(9):
            if board[k][j] == num:
                return False

        start_r = (i // 3) * 3
        start_c = (j // 3) * 3
        for r in range(start_r, start_r + 3):
            for c in range(start_c, start_c + 3):
                if board[r][c] == num:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    sol.solveSudoku(board)
    pprint(board)