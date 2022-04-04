from random import randint
from typing import List
from pprint import pprint


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j))

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while len(q) > 0:
            x, y = q[0]
            for step_x, step_y in directions:
                next_x = x + step_x
                next_y = y + step_y
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                    if grid[next_x][next_y] == 0:
                        grid[next_x][next_y] = grid[x][y] + 1
                        q.append((next_x, next_y))
            q = q[1:]
        # print(grid)
        flatten = [dis for line in grid for dis in line]
        if 2 in flatten:    # at least one 0 in grid
            return max(flatten) - 1
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    n = 100
    grid = [[randint(0, 1) for _ in range(n)] for __ in range(n)]
    print(grid)
    # grid = [[1,0,0],[0,0,0],[0,0,0]]
    print(sol.maxDistance(grid))
