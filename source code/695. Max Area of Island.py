from typing import List
from pprint import pprint


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(grid, i, j))
        return res

    def dfs(self, grid, x, y):
        area = 0
        if grid[x][y] != 1:
            return area
        area += 1
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        grid[x][y] = 2
        for step_x, step_y in directions:
            next_x = x + step_x
            next_y = y + step_y
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                area += self.dfs(grid, next_x, next_y)
        return area


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 0, 1], [0, 1, 0]]
    print(sol.maxAreaOfIsland(grid))
