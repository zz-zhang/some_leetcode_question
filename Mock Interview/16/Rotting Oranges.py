from typing import *
from pprint import pprint

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        res = 0
        while True:
            res += 1
            new_grid = [[item for item in row] for row in grid]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        for x, y in directions:
                            if 0 <= i + x < len(grid):
                                if grid[i + x][j] == 1:
                                    new_grid[i + x][j] = 2
                            if 0 <= j + y < len(grid[0]):
                                if grid[i][j + y] == 1:
                                    new_grid[i][j + y] = 2
            # pprint(new_grid)
            finish, able_to_reach = self.finished(grid, new_grid)
            if finish:
                if able_to_reach:
                    return res - 1
                else:
                    return -1
            
            grid = new_grid


    def finished(self, grid, new_grid):
        able_to_reach = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if new_grid[i][j] == 1:
                    able_to_reach = False
                if grid[i][j] != new_grid[i][j]:
                    return False, able_to_reach
        return True, able_to_reach

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,2]]
    print(sol.orangesRotting(grid))