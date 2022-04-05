from pprint import pprint
from typing import List
from random import randint

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        directions = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]
        q = [(0, 0, 1)]
        grid[0][0] = 1
        while len(q) > 0:
            i, j, num = q[0]
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return num
            for step_i, step_j in directions:
                next_i = i + step_i
                next_j = j + step_j
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                    if grid[next_i][next_j] == 0:
                        grid[next_i][next_j] = 1
                        q.append((next_i, next_j, num + 1))
            # print(len(q))
            q = q[1:]
        return -1


if __name__ == '__main__':
    sol = Solution()
    n = 20
    grid = [[randint(0, 1) for _ in range(n)] for __ in range(n)]
    grid[0][0] = 0
    grid[-1][-1] = 0
    print(grid)
    print(sol.shortestPathBinaryMatrix(grid))
    # pprint(grid)