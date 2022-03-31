from pprint import pprint
from typing import List


class Solution:

    def closedIsland(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # print(i, j)
                    # breakpoint()
                    if self.dfs(grid, i, j):
                        count += 1
        # pprint(grid)
        return count

    def dfs(self, grid, x, y):
        if grid[x][y] != 0:
            return True
        close_flag = True
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        grid[x][y] = 2
        if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
            close_flag = False
        for step_x, step_y in directions:
            next_x = x + step_x
            next_y = y + step_y
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                close_flag = self.dfs(grid, next_x, next_y) and close_flag
        return close_flag


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0,
                                    1], [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]
    print(sol.closedIsland(grid))