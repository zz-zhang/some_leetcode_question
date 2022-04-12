from pprint import pprint
from typing import List
from random import randint

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]
        # print(directions)
        prev_board = [[status for status in line] for line in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                num_neighboor = 0
                for step_i, step_j in directions:
                    neigh_i = i + step_i
                    neigh_j = j + step_j
                    if 0 <= neigh_i < len(board) and 0 <= neigh_j < len(board[0]):
                        num_neighboor += prev_board[neigh_i][neigh_j]
                if board[i][j] == 1:
                    if num_neighboor < 2:
                        board[i][j] = 0
                    elif 2 <= num_neighboor <= 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if num_neighboor == 3:
                        board[i][j] = 1

if __name__ == '__main__':
    sol = Solution()
    n = randint(0, 25)
    m = randint(0, 25)
    board = [[randint(0, 1) for __ in range(m)] for _ in range(n)]
    print(board)
    sol.gameOfLife(board)
    # pprint(board)