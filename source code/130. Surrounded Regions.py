from typing import List
from pprint import pprint


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[False for _ in range(len(board[0]))] for __ in range(len(board))]
        for idx_r, row in enumerate(board):
            for idx_c, mark in enumerate(row):
                if mark == 'O' and not visited[idx_r][idx_c]:
                    visited[idx_r][idx_c] = True
                    self.check_flip(board, idx_r, idx_c, visited)

    def check_flip(self, board, i, j, visited):
        # breakpoint()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        region_indices = [(i, j)]
        q = [(i, j)]
        while q:
            x, y = q.pop(0)
            for delta_x, delta_y in directions:
                if 0 <= x + delta_x < len(board) and 0 <= y + delta_y < len(board[0]):
                    if board[x + delta_x][y + delta_y] == 'O' and not visited[x + delta_x][y + delta_y]:
                        q.append((x + delta_x, y + delta_y))
                        visited[x + delta_x][y + delta_y] = True
                        region_indices.append((x + delta_x, y + delta_y))
        
        # check whether exist mark on edges
        for x, y in region_indices:
            if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                return
        else:
            for x, y in region_indices:
                board[x][y] = 'X'


if __name__ == '__main__':
    sol = Solution()
    board = [["X", "X", "X", "X"], 
             ["X", "O", "O", "X"], 
             ["X", "X", "O", "X"],
             ["X", "O", "O", "X"]]
    # board = [['X']]
    sol.solve(board)
    pprint(board)